#-*- coding:utf-8 -*-
import tensorflow as tf

# 第一个是参数名称，第二个参数是默认值，第三个是参数描述

tf.app.flags.DEFINE_string('str_name', 'def_v_1', "descrip1")
tf.app.flags.DEFINE_integer('int_name', 10, "descript2")
tf.app.flags.DEFINE_boolean('bool_name', False, "descript3")

FLAGS = tf.app.flags.FLAGS


tf.flags.DEFINE_string("input_dir", "./data", "Directory containing input data files 'train.tfrecords' and 'validation.tfrecords'")
tf.flags.DEFINE_string("model_dir", None, "Directory to store model checkpoints (defaults to ./runs)")
tf.flags.DEFINE_integer("loglevel", 20, "Tensorflow log level")
tf.flags.DEFINE_integer("num_epochs", None, "Number of training Epochs. Defaults to indefinite.")
tf.flags.DEFINE_integer("eval_every", 2000, "Evaluate after this many train steps")


def main(_):

    print(FLAGS.str_name)
    print(FLAGS.int_name)
    print(FLAGS.bool_name)

    print(FLAGS.input_dir)


if __name__ == '__main__':
    tf.app.run()  # 执行main函数