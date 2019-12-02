from keras.callbacks import ModelCheckpoint, TensorBoard

import LoadBatches
from Models import FCN8, FCN32, SegNet, UNet
from keras import optimizers
import math
import tensorflow as tf

#############################################################################
train_images_path = "data/dataset/train/org_grid/"
train_segs_path = "data/dataset/train/gt_indx/"
train_batch_size = 32
n_classes = 6

epochs = 50

input_height = 224
input_width = 224


val_images_path = "data/dataset/test/org_grid/"
val_segs_path = "data/dataset/test/gt_indx/"
val_batch_size = 32

key = "fcn8"


##################################

method = {
    "fcn32": FCN32.FCN32,
    "fcn8": FCN8.FCN8,
    'segnet': SegNet.SegNet,
    'unet': UNet.UNet}
def balanced_cross_entropy(y_true, y_pred, beta=0.6):
    # see https://github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py#L3525
    y_pred = tf.clip_by_value(y_pred, tf.keras.backend.epsilon(), 1 - tf.keras.backend.epsilon())

    y_pred = tf.log(y_pred / (1 - y_pred))
    pos_weight = beta / (1 - beta)
    loss = tf.nn.weighted_cross_entropy_with_logits(logits=y_pred, targets=y_true, pos_weight=pos_weight)

    return loss * (1 - beta)

def weighted_cross_entropy(y_true, y_pred, beta=.5):
      # see https://github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py#L3525
    y_pred = tf.clip_by_value(y_pred, tf.keras.backend.epsilon(), 1 - tf.keras.backend.epsilon())

    y_pred = tf.log(y_pred / (1 - y_pred))
    pos_weight = beta / (1 - beta)
    loss = tf.nn.weighted_cross_entropy_with_logits(logits=y_pred, targets=y_true, pos_weight=pos_weight)

    return loss 

sgd = optimizers.SGD(lr=1E-2, decay=5**(-4), momentum=0.9, nesterov=True)

m = method[key](n_classes, input_height=input_height, input_width=input_width)
m.compile(
    loss=balanced_cross_entropy,
    optimizer=sgd,
    metrics=['acc'])

G = LoadBatches.imageSegmentationGenerator(train_images_path,
                                           train_segs_path, train_batch_size, n_classes=n_classes, input_height=input_height, input_width=input_width)

G_test = LoadBatches.imageSegmentationGenerator(val_images_path,
                                                val_segs_path, val_batch_size, n_classes=n_classes, input_height=input_height, input_width=input_width)

checkpoint = ModelCheckpoint(
    filepath="output/%s_model_sgd_bal.h5" %
    key,
    monitor='acc',
    mode='auto',
    save_best_only='True')
tensorboard = TensorBoard(log_dir='output/log_%s_bal_model' % key, histogram_freq=0, batch_size=32, write_graph=True, write_grads=True, write_images=True, embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None, embeddings_data=None, update_freq='batch')


# checkpoint = ModelCheckpoint(
#     filepath="output/%smodel_sgd_balanced.h5" %
#     key,
#     monitor='acc',
#     mode='auto',
#     save_best_only='True')
# tensorboard = TensorBoard(log_dir='output/log_%s_model' % key, histogram_freq=0, batch_size=32, write_graph=True, write_grads=True, write_images=True, embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None, embeddings_data=None, update_freq='batch')

m.fit_generator(generator=G,
                steps_per_epoch=math.ceil(115200. / train_batch_size),
                epochs=epochs, callbacks=[checkpoint, tensorboard],
                verbose=1,
                validation_data=G_test,
                validation_steps=math.ceil(28800. / val_batch_size),
                shuffle=True)
