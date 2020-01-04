from gluon.datasets.imports import *
from system.imports import *



class DatasetCustom(Dataset):
    @accepts("self", list, list, str, post_trace=True)
    @TraceFunction(trace_args=False, trace_rv=False)
    def __init__(self, img_list, label_list, prefix):
        self.img_list = img_list;
        self.label_list = label_list;
        self.prefix = prefix;
    
    @accepts("self", post_trace=True)
    @TraceFunction(trace_args=False, trace_rv=False)    
    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self, index):
        image_name = self.prefix + "/" + self.img_list[index];
        img = image.imread(image_name);
        label = int(self.label_list[index]);       
        return img, label

