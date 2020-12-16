from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import sys
import os
import os.path as osp

import numpy as np
import glob
from torchreid.data import ImageDataset

# Load Our Dataset to DataLoader
class CvDataSet(ImageDataset):
    dataset_dir = 'reid-data'

    def __init__(self, root='', **kwargs):
        #self.root = osp.abspath(osp.expanduser(root))
        self.root = os.getcwd()
        self.dataset_dir = osp.join(self.root, self.dataset_dir, 'data')
        print('self.dataset_dir', self.dataset_dir)
        self.train_dir = osp.join(self.dataset_dir, 'cv_dataset')
        self.query_dir = osp.join(self.dataset_dir, 'cv_dataset', 'query')
        self.gallery_dir = osp.join(self.dataset_dir, 'cv_dataset', 'gallery')

        train = self.process_dir(self.train_dir)
        query = self.process_dir(self.query_dir)
        gallery = self.process_dir(self.gallery_dir)

        super(CvDataSet, self).__init__(train, query, gallery, **kwargs)

    def process_dir(self, dir_path):
      data = []
      for root, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
          if filename.endswith(('.jpg')):
            fname = os.path.join(root, filename)
            if (filename[0]) == '-':
              pid, cid, _, _ = filename.split("_")
            else:
              pid, cid, _ = filename.split("_")
            
            fname, c, p = os.path.join(root, filename), int(cid[1]), int(pid)
            data.append((fname, c, p))
        
      return data
