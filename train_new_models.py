from ISR.models import RRDN
from ISR.models import Discriminator
from ISR.models import Cut_VGG19

lr_train_patch_size = 40
layers_to_extract = [5, 9]
scale = 3
hr_train_patch_size = lr_train_patch_size * scale

rrdn  = RRDN(arch_params={'C':4 , 'D':3, 'G':64, 'G0':64, 'T':10, 'x':scale}, patch_size=lr_train_patch_size)
f_ext = Cut_VGG19(patch_size=hr_train_patch_size, layers_to_extract=layers_to_extract)
discr = Discriminator(patch_size=hr_train_patch_size, kernel_size=3)

from ISR.train import Trainer
loss_weights = {
  'generator': 0.0,
  'feature_extractor': 0.0833,
  'discriminator': 0.01
}
losses = {
  'generator': 'mae',
  'feature_extractor': 'mse',
  'discriminator': 'binary_crossentropy'
} 

log_dirs = {'logs': './logs', 'weights': './weights'}

learning_rate = {'initial_value': 0.0004, 'decay_factor': 0.5, 'decay_frequency': 30}

flatness = {'min': 0.0, 'max': 0.15, 'increase': 0.01, 'increase_frequency': 5}

trainer = Trainer(
    generator=rrdn,
    discriminator=discr,
    feature_extractor=f_ext,
    lr_train_dir='../data/train_lr_img_small/',
    hr_train_dir='../data/train_hr_img/',
    lr_valid_dir='../data/val_lr_img_small/',
    hr_valid_dir='../data/val_hr_img/',
    loss_weights=loss_weights,
    learning_rate=learning_rate,
    flatness=flatness,
    dataname='data',
    log_dirs=log_dirs,
    weights_generator=None,
    weights_discriminator=None,
    n_validation=200,
)

trainer.train(
    epochs=1000,
    steps_per_epoch=2000//4,
    batch_size=4,
    monitored_metrics={'val_generator_PSNR_Y': 'max'}
)