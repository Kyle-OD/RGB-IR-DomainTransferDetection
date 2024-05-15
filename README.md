# RGB-IR-DomainTransferDetection

Clone the following repos into your parent directory:
```bash
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
git clone https://github.com/ultralytics/yolov5
```


Download datasets:
- LLVIP[https://github.com/bupt-ai-cz/LLVIP]: Paired Visible-Thermal image dataset for streetview
- COCO2017[https://cocodataset.org/#home]: Common Objects in Contect

Training VAE on LLVIP:


Training Pix2pix on LLVIP:
python pytorch-CycleGAN-and-pix2pix/train.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot ./data/LLVIP/visible-infrared/ --name LLVIP2 --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --n_epochs 100 --n_epochs_decay 100 --netG unet_256

Transfer COCO to Thermal with pix2pix:
(Train)
```
python pytorch-CycleGAN-and-pix2pix/test.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot data/coco/train2017/ --phase '' --name LLVIP2 --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --netG unet_256 --results_dir data/coco-ir-pix2pix/train2017/ --num_test 118287
```
(Validation)
```
python pytorch-CycleGAN-and-pix2pix/test.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot data/coco/val2017/ --phase '' --name LLVIP2 --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --netG unet_256 --results_dir data/coco-ir-pix2pix/val2017/ --num_test 5000
```
(Test)
```
python pytorch-CycleGAN-and-pix2pix/test.py --checkpoints_dir pytorch-CycleGAN-and-pix2pix/checkpoints/ --dataroot data/coco/test2017/ --phase '' --name LLVIP2 --model pix2pix --direction AtoB --batch_size 8 --preprocess scale_width_and_crop --load_size 320 --crop_size 256 --gpu_ids 0 --netG unet_256 --results_dir data/coco-ir-pix2pix/test2017/ --num_test 40670
```
Retrain Yolo-v5