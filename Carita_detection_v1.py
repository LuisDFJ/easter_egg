import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

from utils import ops as utils_ops
from utils import label_map_util
from utils import visualization_utils as vis_util

utils_ops.tf = tf.compat.v1
tf.gfile = tf.io.gfile

def load_model(src_model):
  model = tf.saved_model.load(src_model)
  model = model.signatures['serving_default']
  return model


def run_inference_for_single_image(model, image):
  image = np.asarray(image)
  input_tensor = tf.convert_to_tensor(image)
  input_tensor = input_tensor[tf.newaxis,...]
  output_dict = model(input_tensor)
  num_detections = int(output_dict.pop('num_detections'))
  output_dict = {key:value[0, :num_detections].numpy()
                 for key,value in output_dict.items()}

  output_dict['num_detections'] = num_detections
  output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
  return output_dict


def show_inference(model, image_path,category_index):
  image_np = np.array(Image.open(image_path))
  output_dict = run_inference_for_single_image(model, image_np)
  vis_util.visualize_boxes_and_labels_on_image_array(
      image_np,
      output_dict['detection_boxes'],
      output_dict['detection_classes'],
      output_dict['detection_scores'],
      category_index,
      instance_masks=output_dict.get('detection_masks_reframed', None),
      use_normalized_coordinates=True,
      line_thickness=8)
  image_d = Image.fromarray(image_np)
  image_d.show()
  return output_dict['detection_classes'][0:3],output_dict['detection_scores'][0:3]


def img_det(PATH_TO_LABELS,PATH_TO_IMAGE,PATH_TO_MODEL):
  src_root = os.getcwd()

  src_model = os.path.join(src_root,PATH_TO_MODEL,'saved_model')
  category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
  TEST_IMAGE_PATHS = os.path.join(src_root,PATH_TO_IMAGE)

  model = load_model(src_model)
  return show_inference(model, TEST_IMAGE_PATHS,category_index)
