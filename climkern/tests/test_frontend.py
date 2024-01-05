from climkern.frontend import *
import xarray as xr

ctrl, pert = tutorial_data('ctrl'),tutorial_data('pert')

def test_calc_T_feedbacks() -> None:
    LR,Planck = calc_T_feedbacks(ctrl.T,ctrl.TS,ctrl.PS,
                                pert.T,pert.TS,pert.PS,pert.TROP_P,
                                kern="GFDL")
    dTS_glob_avg = spat_avg(pert.TS - ctrl.TS)
    LR_val = (spat_avg(LR)/dTS_glob_avg).mean()
    Planck_val = (spat_avg(Planck)/dTS_glob_avg).mean()
    xr.testing.assert_allclose(LR_val,xr.DataArray(-0.41),atol=0.01)
    xr.testing.assert_allclose(Planck_val,xr.DataArray(-3.12),atol=0.01)