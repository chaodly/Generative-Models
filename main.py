import io
import os
import sys
import time
import argparse
from time import gmtime, strftime
import tensorflow as tf

import nnet
import utils

import nnet
from options import Options 

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

FLAGS = tf.app.flags.FLAGS

# Model
tf.app.flags.DEFINE_string('model', 'vae', """vae or gan""")

# Data
tf.app.flags.DEFINE_string('root_dir', '/users/TeamVideoSummarization/gsoc/Generative-models/', """Base Path""")
tf.app.flags.DEFINE_string('dataset_dir', 'data/', """Path to data""")
tf.app.flags.DEFINE_integer('image_size_h', 32, """Shape of image height""")
tf.app.flags.DEFINE_integer('image_size_w', 32, """Shape of image width""")
tf.app.flags.DEFINE_integer('channels', 3, """Number of input channels of images""")
tf.app.flags.DEFINE_string('dataset', "mnist", """mnist or CIFAR""")

# Training
tf.app.flags.DEFINE_integer('batch_size', 64, """Batch size""")
tf.app.flags.DEFINE_integer('MAX_iterations', 1000, """Max iterations for training""")
tf.app.flags.DEFINE_integer('decay_after', 20, """Decay learning after iterations""")
tf.app.flags.DEFINE_integer('ckpt_frq', 150, """Frequency at which to checkpoint the model""")
tf.app.flags.DEFINE_integer('train_size', 10000, """The total training size""")
tf.app.flags.DEFINE_integer('generate_frq', 100, """The frequency with which to sample images""")
tf.app.flags.DEFINE_integer('test_size', 64, """Number of images to sample during test phase""")
tf.app.flags.DEFINE_integer('display', 60, """Display log of progress""")
tf.app.flags.DEFINE_float('lr_decay', 0.9, """Learning rate decay factor""")
tf.app.flags.DEFINE_float('base_lr', 1e-6, """Base learning rate for VAE""")
tf.app.flags.DEFINE_float('D_base_lr', 1e-6, """Base learning rate for Discriminator""")
tf.app.flags.DEFINE_float('G_base_lr', 1e-6, """Base learning rate for Generator""")
tf.app.flags.DEFINE_float('D_lambda', 1, """How much to weigh in Decoder loss""")
tf.app.flags.DEFINE_float('G_lambda', 1, """How much to weigh in Generator loss""")


# Architecture
tf.app.flags.DEFINE_integer('encoder_vec_size', 100, """Encoder vector size for VAE""")
tf.app.flags.DEFINE_integer('latent_shape', 100, """Latent code length in case of GAN""")
tf.app.flags.DEFINE_integer('g_dims', 64, """Number of kernels for the first convolutional lalyer in the network""")

# Model Saving
tf.app.flags.DEFINE_string('ckpt_dir', "ckpt/", """Checkpoint Directory""")
tf.app.flags.DEFINE_string('sample_dir', "imgs/", """Generate sample images""")
tf.app.flags.DEFINE_string('summary_dir', "summary/", """Summaries directory""")
tf.app.flags.DEFINE_integer('grid_h', 8, """Grid height while saving images""")
tf.app.flags.DEFINE_integer('grid_w', 8, """Grid width while saving images""")


def main(_):
	print 'Beginning Run'
	net = nnet.VAE(FLAGS, True)
	print 'Training the network...'
	net.train()
	print 'Done training the network...\n'
		

if __name__ == '__main__':
	try:
		tf.app.run()
	except Exception as E:
		print E