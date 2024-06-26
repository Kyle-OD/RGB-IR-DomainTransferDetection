# RGB-IR-DomainTransferDetection

## Install Dependencies

This project uses anaconda to manage packages.  To install required libraries, rn the following command from terminal:

```
conda env create -f environment.yml
```

Activate this environment with `conda activate rgb-ir`

### Install dependant directories
Clone the following repos into your parent directory:
```
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
git clone https://github.com/ultralytics/yolov5
```

Follow steps that each directory required for setup, located in their respective README.md files

### Datasets 
Download datasets:
- LLVIP[https://github.com/bupt-ai-cz/LLVIP]: Paired Visible-Thermal image dataset for streetview
- COCO2017[https://cocodataset.org/#home]: Common Objects in Contect

Move to directory `./data`

### Prepare paired visible-thermal images
```
python pytorch-CycleGAN-and-pix2pix/datasets/combine_A_and_B.py --fold_A data/LLVIP/visible/ --fold_B data/LLVIP/infrared/ --foldAB data/LLVIP/visible-infrared/
```

## Train VAE for image-image translation
1) Run the cells in `VAE_transfer.ipynb` 
2) More ablations and architecture changes needed


## Training Pix2pix VAE for image-image translation
```
python pytorch-CycleGAN-and-pix2pix/train.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot ./data/LLVIP/visible-infrared/ --name LLVIP --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --n_epochs 100 --n_epochs_decay 100 --netG unet_256
```

To plot the loss of training, use the code located in `plot_p2p_loss.ipynb`

## Transfer COCO to Thermal with pix2pix:
### Train
```
python pytorch-CycleGAN-and-pix2pix/test.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot data/coco/train2017/ --phase '' --name LLVIP --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --netG unet_256 --results_dir data/coco-ir-pix2pix/train2017/ --num_test 118287
```

### Validation
```
python pytorch-CycleGAN-and-pix2pix/test.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot data/coco/val2017/ --phase '' --name LLVIP --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --netG unet_256 --results_dir data/coco-ir-pix2pix/val2017/ --num_test 5000
```

### Test
```
python pytorch-CycleGAN-and-pix2pix/test.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot data/coco/test2017/ --phase '' --name LLVIP --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --netG unet_256 --results_dir data/coco-ir-pix2pix/test2017/ --num_test 40670
```

To fix directory structure, run the following:
```
python move_transferred_im.py
```

## Retrain Yolo-v5
install yolo model weights
```
bash ./yolov5/data/scripts/download_weights.sh
```

Train new model
```
cp coco-ir.yaml ./yolov5/data/
python yolov5/train.py --data coco-ir.yaml --weights yolov5s.pt --imgsz 640 --epochs 30
```

Use instructions from `yolov5/README.md` to evaluate new model on translated images