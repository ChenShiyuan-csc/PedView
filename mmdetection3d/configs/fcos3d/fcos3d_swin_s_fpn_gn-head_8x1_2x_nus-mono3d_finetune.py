_base_ = './fcos3d_swin_s_2x.py'
# model settings
model = dict(
    train_cfg=dict(
        code_weight=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.05, 0.05]))
# optimizer
optimizer = dict(lr=0.0005)

