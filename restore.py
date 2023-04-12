#%%
import tensorflow as tf
import pandas as pd
import csv
import os
import argparse
import matplotlib.pyplot as plt
import numpy as np
import DGM2
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#%%

w1 = tf.Variable(tf.random_normal(shape=[2]), name='w1')
w2 = tf.Variable(tf.random_normal(shape=[5]), name='w2')
saver = tf.train.Saver([w1, w2])
sess = tf.Session()
sess.run(tf.global_variables_initializer())
saver.save(sess, './SavedNets/my_test_model', global_step=1000)


# %%
