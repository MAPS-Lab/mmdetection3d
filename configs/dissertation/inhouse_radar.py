_base_ = 'pointpillars_inhouse-3class_radar.py'

# Model setup
data_root = 'data/inhouse_radar_only/kitti_format/'

# Experiment settings
runner = dict(max_epochs=160)
evaluation = dict(interval=4)

data = dict(samples_per_gpu=11, workers_per_gpu=4)
