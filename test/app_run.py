import tensorflow as tf

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('string', 'train', 'This is a string')
tf.app.flags.DEFINE_float('learning_rate', 0.001, 'This is the rate in training')
tf.app.flags.DEFINE_boolean('flag', True, 'This is a flag')

print('string: ', FLAGS.string)
print('learning_rate: ', FLAGS.learning_rate)
print('flag: ', FLAGS.flag)