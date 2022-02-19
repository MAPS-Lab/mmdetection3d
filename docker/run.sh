docker run -it --rm --ipc=host\
    -v /mnt/sda1/DJ/code:/code \
    -v /mnt/sda1/DJ/data:/data \
    -v /mnt/12T/public:/public \
    -v /mnt/sda1/DJ/code/mmdetection3d:/mmdetection3d \
    --gpus all\
    --name centerpoint \
    mmdet:centerpoint
