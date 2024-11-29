#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openmc sources  
    targets : Be, Ta, 
    proton energy : 25MeV, 40MeV
    particles : neutrons or photons

from sources_icone import sourceBe25, sourceTa25, sourceBe40, sourceTa40
from sources_icone import gamma_sourceBe25, gamma_sourceBe40, gamma_sourceTa25, gamma_sourceTa40

Created 2024.03.01  09:47:14 
updated 2024.03.12  15:36
        2024.05.17 gamma_sources added 
        2024.06.12 add source_run_test
        
run sources_icone.py to plot a test_source       
@author: jdarpentigny
"""

import openmc
import numpy as np
# from openmc import Source                     # openmc 0.13
from openmc import IndependentSource as Source  # openmc 0.14
    
def sourceBe25(openmc_space, strength = 4.4E14, uvw = (0., 0., 1.)):
    """an OpenMC Source for Be target hit by 25MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (4.4E14 for 80KW, 25MeV proton beam on Be)
    uvw : Iterable of float, optional   
        Direction of proton beam

    
    Returns
    -------
    openmc.Source (list of openmc.SourceBase object)
        Distribution of phase space coordinates for source sites.

    """
    # Be 25MeV 
    # openmc_space = openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
    # strength = 4.4E14 # Be, 25MeV, 80KW # nb fast neutron produced 
    # uvw = (0., 0., 1.) # reference_uvw of proton beam
    
    phi = openmc.stats.Uniform(0.0, 2 * np.pi) # 
    erg_bins = [316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0]
    
    cos_bins_0 = [-1, -0.9, -0.8, -0.7]
    angular_distrib_0 = [0.3421, 0.3277, 0.3302, 0]
    erg_distrib_0 = [0.1284, 0.1053, 0.0942, 0.0806, 0.0619, 0.0593, 0.0607, 0.0638, 0.0955, 0.0711, 0.0481, 0.0435, 0.0356, 0.0266, 0.0153, 0.0081, 0.0023, 0.0, 0.0, 0.0, 0]
    cos0 = openmc.stats.Tabular(cos_bins_0, angular_distrib_0, interpolation='histogram')
    angle0 = openmc.stats.PolarAzimuthal(mu= cos0, phi= phi, reference_uvw= uvw)
    energy0 = openmc.stats.Tabular(erg_bins, erg_distrib_0, interpolation='histogram')
    strength0 = strength * 0.0788
    source0 = Source(space= openmc_space, angle= angle0, energy= energy0, strength= strength0)
    
    cos_bins_1 = [-0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -1.94289e-16]
    angular_distrib_1 = [0.12, 0.1259, 0.1303, 0.1407, 0.1508, 0.1601, 0.1722, 0]
    erg_distrib_1 = [0.1736, 0.1622, 0.1219, 0.076, 0.065, 0.0486, 0.0414, 0.0413, 0.0462, 0.0595, 0.0499, 0.0338, 0.0308, 0.0229, 0.0152, 0.0078, 0.0036, 0.0005, 0.0, 0.0, 0]
    cos1 = openmc.stats.Tabular(cos_bins_1, angular_distrib_1, interpolation='histogram')
    angle1 = openmc.stats.PolarAzimuthal(mu= cos1, phi= phi, reference_uvw= uvw)
    energy1 = openmc.stats.Tabular(erg_bins, erg_distrib_1, interpolation='histogram')
    strength1 = strength * 0.2278
    source1 = Source(space= openmc_space, angle= angle1, energy= energy1, strength= strength1)
    
    cos_bins_2 = [-1.94289e-16, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    angular_distrib_2 = [0.1048, 0.1145, 0.1247, 0.1379, 0.1534, 0.1711, 0.1936, 0]
    erg_distrib_2 = [0.0565, 0.0808, 0.1103, 0.1492, 0.1415, 0.0973, 0.05, 0.0387, 0.0332, 0.0355, 0.0439, 0.0505, 0.0331, 0.0283, 0.0223, 0.0151, 0.0089, 0.0045, 0.0003, 0.0, 0]
    cos2 = openmc.stats.Tabular(cos_bins_2, angular_distrib_2, interpolation='histogram')
    angle2 = openmc.stats.PolarAzimuthal(mu= cos2, phi= phi, reference_uvw= uvw)
    energy2 = openmc.stats.Tabular(erg_bins, erg_distrib_2, interpolation='histogram')
    strength2 = strength * 0.4
    source2 = Source(space= openmc_space, angle= angle2, energy= energy2, strength= strength2)
    
    cos_bins_3 = [0.7, 0.8, 0.9]
    angular_distrib_3 = [0.4782, 0.5218, 0]
    erg_distrib_3 = [0.0436, 0.0397, 0.0384, 0.0382, 0.0868, 0.2008, 0.1611, 0.0606, 0.0404, 0.0362, 0.0396, 0.0456, 0.0545, 0.0359, 0.0311, 0.0233, 0.0141, 0.0085, 0.0018, 0.0, 0]
    cos3 = openmc.stats.Tabular(cos_bins_3, angular_distrib_3, interpolation='histogram')
    angle3 = openmc.stats.PolarAzimuthal(mu= cos3, phi= phi, reference_uvw= uvw)
    energy3 = openmc.stats.Tabular(erg_bins, erg_distrib_3, interpolation='histogram')
    strength3 = strength * 0.181
    source3 = Source(space= openmc_space, angle= angle3, energy= energy3, strength= strength3)
    
    cos_bins_4 = [0.9, 1.0]
    angular_distrib_4 = [1.0, 0]
    erg_distrib_4 = [0.058, 0.0556, 0.0426, 0.0395, 0.0384, 0.1045, 0.2058, 0.1047, 0.0483, 0.0384, 0.0371, 0.0397, 0.0576, 0.0367, 0.0324, 0.0262, 0.0178, 0.0123, 0.0043, 0.0, 0]
    cos4 = openmc.stats.Tabular(cos_bins_4, angular_distrib_4, interpolation='histogram')
    angle4 = openmc.stats.PolarAzimuthal(mu= cos4, phi= phi, reference_uvw= uvw)
    energy4 = openmc.stats.Tabular(erg_bins, erg_distrib_4, interpolation='histogram')
    strength4 = strength * 0.1123
    source4 = Source(space= openmc_space, angle= angle4, energy= energy4, strength= strength4)
    #source = [source0, source1, source2, source3, source4] 
    return [source0, source1, source2, source3, source4]

def sourceTa25(openmc_space , strength = 2E14, uvw = (0., 0., 1.)) :
    """an OpenMC Source for Ta target hit by 25MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (2E14 for 80KW, 25MeV proton beam on Ta)
    uvw : Iterable of float, optional   
        Direction of proton beam

    
    Returns
    -------
    openmc.Source (list of openmc.SourceBase object)
        Distribution of phase space coordinates for source sites.

    """
    # Ta25
    # openmc_space = openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
    # strength = 2E14 # Ta, 25MeV, 80KW # nb fast neutron produced # to be modified
    # uvw = (0., 0., 1.) # reference_uvw of proton beam
    phi = openmc.stats.Uniform(0.0, 2 * np.pi) # 
    erg_bins = [100000.0, 125893.0, 158489.0, 199526.0, 251189.0, 316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0]
    
    cos_bins_0 = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -1.94289e-16]
    angular_distrib_0 = [0.0999, 0.0954, 0.0983, 0.1029, 0.101, 0.0972, 0.103, 0.0989, 0.1014, 0.102, 0]
    erg_distrib_0 = [0.0606, 0.0685, 0.0729, 0.0809, 0.0849, 0.0878, 0.0955, 0.0888, 0.0918, 0.0754, 0.0665, 0.0473, 0.0353, 0.0221, 0.0117, 0.0058, 0.0022, 0.0009, 0.0004, 0.0003, 0.0002, 0.0001, 0.0, 0.0, 0.0, 0]
    cos0 = openmc.stats.Tabular(cos_bins_0, angular_distrib_0, interpolation='histogram')
    angle0 = openmc.stats.PolarAzimuthal(mu= cos0, phi= phi, reference_uvw= uvw)
    energy0 = openmc.stats.Tabular(erg_bins, erg_distrib_0, interpolation='histogram')
    strength0 = strength * 0.4906
    source0 = Source(space= openmc_space, angle= angle0, energy= energy0, strength= strength0)
    
    cos_bins_1 = [-1.94289e-16, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    angular_distrib_1 = [0.0962, 0.0946, 0.0979, 0.103, 0.0998, 0.1012, 0.0988, 0.1041, 0.1029, 0.1014, 0]
    erg_distrib_1 = [0.056, 0.0665, 0.0633, 0.0792, 0.0821, 0.0892, 0.0893, 0.0953, 0.0835, 0.0807, 0.07, 0.0533, 0.0381, 0.0247, 0.0128, 0.0072, 0.0034, 0.0018, 0.0012, 0.0009, 0.0008, 0.0005, 0.0003, 0.0, 0.0, 0]
    cos1 = openmc.stats.Tabular(cos_bins_1, angular_distrib_1, interpolation='histogram')
    angle1 = openmc.stats.PolarAzimuthal(mu= cos1, phi= phi, reference_uvw= uvw)
    energy1 = openmc.stats.Tabular(erg_bins, erg_distrib_1, interpolation='histogram')
    strength1 = strength * 0.5094
    source1 = Source(space= openmc_space, angle= angle1, energy= energy1, strength= strength1)
    #source = [source0, source1] 
    return [source0, source1,]

def sourceBe40(openmc_space, strength = 6.125E14, uvw = (0., 0., 1.)):
    """an OpenMC Source for Be target hit by 40MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (6.125E14 for 80KW, 40MeV proton beam on Be)
    uvw : Iterable of float, optional   
        Direction of proton beam

    
    Returns
    -------
    openmc.Source (list of openmc.SourceBase object)
        Distribution of phase space coordinates for source sites.

    """
    # Be 40MeV 


    phi = openmc.stats.Uniform(0.0, 2 * np.pi) # 
    erg_bins = [316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0, 39810700.0]
    
    
    cos_bins_0 = [-1, -0.9, -0.8, -0.7]
    angular_distrib_0 = [0.3286, 0.3321, 0.3393, 0]
    erg_distrib_0 = [0.1314, 0.1203, 0.0991, 0.0927, 0.0763, 0.0589, 0.0543, 0.0641, 0.0863, 0.0523, 0.0383, 0.0355, 0.0294, 0.0237, 0.0164, 0.0101, 0.0056, 0.0037, 0.0016, 0.0, 0.0, 0]
    cos0 = openmc.stats.Tabular(cos_bins_0, angular_distrib_0, interpolation='histogram')
    angle0 = openmc.stats.PolarAzimuthal(mu= cos0, phi= phi, reference_uvw= uvw)
    energy0 = openmc.stats.Tabular(erg_bins, erg_distrib_0, interpolation='histogram')
    strength0 = strength * 0.0789
    source0 = Source(space= openmc_space, angle= angle0, energy= energy0, strength= strength0)
    
    
    cos_bins_1 = [-0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -1.94289e-16]
    angular_distrib_1 = [0.1208, 0.1253, 0.1333, 0.1394, 0.1488, 0.1606, 0.1719, 0]
    erg_distrib_1 = [0.1529, 0.1448, 0.1042, 0.0849, 0.0733, 0.0594, 0.0481, 0.0466, 0.0514, 0.0604, 0.0471, 0.0328, 0.0288, 0.0237, 0.0178, 0.0114, 0.0063, 0.0036, 0.0021, 0.0006, 0.0, 0]
    cos1 = openmc.stats.Tabular(cos_bins_1, angular_distrib_1, interpolation='histogram')
    angle1 = openmc.stats.PolarAzimuthal(mu= cos1, phi= phi, reference_uvw= uvw)
    energy1 = openmc.stats.Tabular(erg_bins, erg_distrib_1, interpolation='histogram')
    strength1 = strength * 0.2213
    source1 = Source(space= openmc_space, angle= angle1, energy= energy1, strength= strength1)
    
    
    cos_bins_2 = [-1.94289e-16, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    angular_distrib_2 = [0.105, 0.113, 0.1246, 0.1374, 0.1529, 0.1724, 0.1948, 0]
    erg_distrib_2 = [0.0901, 0.1028, 0.1095, 0.1264, 0.1189, 0.0869, 0.0512, 0.0371, 0.0321, 0.0322, 0.04, 0.0458, 0.0315, 0.0258, 0.0219, 0.0172, 0.0119, 0.0081, 0.0061, 0.0041, 0.0005, 0]
    cos2 = openmc.stats.Tabular(cos_bins_2, angular_distrib_2, interpolation='histogram')
    angle2 = openmc.stats.PolarAzimuthal(mu= cos2, phi= phi, reference_uvw= uvw)
    energy2 = openmc.stats.Tabular(erg_bins, erg_distrib_2, interpolation='histogram')
    strength2 = strength * 0.3918
    source2 = Source(space= openmc_space, angle= angle2, energy= energy2, strength= strength2)
    
    
    cos_bins_3 = [0.7, 0.8, 0.9]
    angular_distrib_3 = [0.4675, 0.5325, 0]
    erg_distrib_3 = [0.0554, 0.0601, 0.0518, 0.0547, 0.0762, 0.1473, 0.1551, 0.0716, 0.0348, 0.0293, 0.033, 0.0381, 0.0511, 0.031, 0.0282, 0.0239, 0.0186, 0.0139, 0.0116, 0.0106, 0.0039, 0]
    cos3 = openmc.stats.Tabular(cos_bins_3, angular_distrib_3, interpolation='histogram')
    angle3 = openmc.stats.PolarAzimuthal(mu= cos3, phi= phi, reference_uvw= uvw)
    energy3 = openmc.stats.Tabular(erg_bins, erg_distrib_3, interpolation='histogram')
    strength3 = strength * 0.1859
    source3 = Source(space= openmc_space, angle= angle3, energy= energy3, strength= strength3)
    
    
    cos_bins_4 = [0.9, 1.0]
    angular_distrib_4 = [1.0, 0]
    erg_distrib_4 = [0.062, 0.0622, 0.0493, 0.0484, 0.0508, 0.0746, 0.1525, 0.1346, 0.0512, 0.0287, 0.0312, 0.0348, 0.0503, 0.0346, 0.0297, 0.0258, 0.0221, 0.0174, 0.0151, 0.0161, 0.0084, 0]
    cos4 = openmc.stats.Tabular(cos_bins_4, angular_distrib_4, interpolation='histogram')
    angle4 = openmc.stats.PolarAzimuthal(mu= cos4, phi= phi, reference_uvw= uvw)
    energy4 = openmc.stats.Tabular(erg_bins, erg_distrib_4, interpolation='histogram')
    strength4 = strength * 0.122
    source4 = Source(space= openmc_space, angle= angle4, energy= energy4, strength= strength4)
    return [source0, source1, source2, source3, source4]

def sourceTa40(openmc_space, strength = 5.25E14, uvw = (0., 0., 1.)):
    """an OpenMC Source for Ta target hit by 40MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (5.25E14 for 80KW, 40MeV proton beam on Ta)
    uvw : Iterable of float, optional   
        Direction of proton beam

    
    Returns
    -------
    openmc.Source (list of openmc.SourceBase object)
        Distribution of phase space coordinates for source sites.

    """
# Ta 40MeV 
    phi = openmc.stats.Uniform(0.0, 2 * np.pi) # 
    erg_bins = [100000.0, 125893.0, 158489.0, 199526.0, 251189.0, 316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0]
    
    
    cos_bins_0 = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, -1.94289e-16]
    angular_distrib_0 = [0.0978, 0.0977, 0.0967, 0.0995, 0.0993, 0.1028, 0.1017, 0.1013, 0.1023, 0.1009, 0]
    erg_distrib_0 = [0.0491, 0.0654, 0.0702, 0.0773, 0.0825, 0.0889, 0.0904, 0.0887, 0.0853, 0.078, 0.0688, 0.0552, 0.0401, 0.0267, 0.0164, 0.0091, 0.0042, 0.0019, 0.0008, 0.0005, 0.0003, 0.0002, 0.0001, 0.0001, 0.0, 0]
    cos0 = openmc.stats.Tabular(cos_bins_0, angular_distrib_0, interpolation='histogram')
    angle0 = openmc.stats.PolarAzimuthal(mu= cos0, phi= phi, reference_uvw= uvw)
    energy0 = openmc.stats.Tabular(erg_bins, erg_distrib_0, interpolation='histogram')
    strength0 = strength * 0.478
    source0 = Source(space= openmc_space, angle= angle0, energy= energy0, strength= strength0)
    
    
    cos_bins_1 = [-1.94289e-16, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    angular_distrib_1 = [0.094, 0.097, 0.0965, 0.0981, 0.0985, 0.0979, 0.1027, 0.1045, 0.1059, 0.1048, 0]
    erg_distrib_1 = [0.0494, 0.0623, 0.0629, 0.0726, 0.0778, 0.0817, 0.0903, 0.0903, 0.087, 0.0814, 0.0718, 0.0578, 0.0434, 0.0286, 0.0181, 0.0106, 0.0053, 0.0028, 0.0016, 0.0012, 0.001, 0.0008, 0.0006, 0.0004, 0.0002, 0]
    cos1 = openmc.stats.Tabular(cos_bins_1, angular_distrib_1, interpolation='histogram')
    angle1 = openmc.stats.PolarAzimuthal(mu= cos1, phi= phi, reference_uvw= uvw)
    energy1 = openmc.stats.Tabular(erg_bins, erg_distrib_1, interpolation='histogram')
    strength1 = strength * 0.522
    source1 = Source(space= openmc_space, angle= angle1, energy= energy1, strength= strength1)
    #source = [source0, source1] 
    return [source0, source1,]


def gamma_sourceBe25(openmc_space, strength = 4.4E14): # isotropic source
    """a gamma OpenMC Source for Be target hit by 25MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (4.4E14 for 80KW, 25MeV proton beam on Be)

    
    Returns
    -------
    openmc.Source (openmc.SourceBase object)
        Energy distribution of photons on source site.


    """
    # from file: G:\gammas\gamma_25MeV_Be_r3.m
    # protons 25 MeV on sphere Be target, r= 3 mm 
    Gammas_per_Proton =  0.0003240734116  # twice the particles of half the angular range
    Neutrons_per_Proton = 0.022161 
    gamma_source_strength = strength * Gammas_per_Proton / Neutrons_per_Proton
    erg_bins = [100000.0, 125893.0, 158489.0, 199526.0, 251189.0, 316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0]
    erg_distrib = [0.0, 0.0, 0.0087, 0.0035, 0.0165, 0.0415, 0.1304, 0.1975, 0.0329, 0.0209, 0.0035, 0.0011, 0.0013, 0.0028, 0.0011, 0.5382, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0]
    energy = openmc.stats.Tabular(erg_bins, erg_distrib, interpolation='histogram')
    return openmc.Source(space= openmc_space, energy= energy, strength= gamma_source_strength, particle='photon')


def gamma_sourceBe40(openmc_space, strength = 6.125E14): # isotropic source
    """a gamma OpenMC Source for Be target hit by 40MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (6.125E14 for 80KW, 40MeV proton beam on Be)

    
    Returns
    -------
    openmc.Source (openmc.SourceBase object)
        Energy distribution of photons on source site.

    """
    # from file: G:\gammas\gamma_40MeV_Be_r9.m
    # protons 40 MeV on sphere Be target, r= 9 mm 
    Gammas_per_Proton =  0.0014849306280000003  # twice the particles of half the angular range
    Neutrons_per_Proton = 0.0488346 
    gamma_source_strength = strength * Gammas_per_Proton / Neutrons_per_Proton
    erg_bins = [100000.0, 125893.0, 158489.0, 199526.0, 251189.0, 316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0]
    erg_distrib = [0.0051, 0.0074, 0.0295, 0.0323, 0.0285, 0.0506, 0.2741, 0.3905, 0.0737, 0.0509, 0.0055, 0.0006, 0.0004, 0.0002, 0.0002, 0.0505, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0]
    energy = openmc.stats.Tabular(erg_bins, erg_distrib, interpolation='histogram')
    return openmc.Source(space= openmc_space, energy= energy, strength= gamma_source_strength, particle='photon')


def gamma_sourceTa25(openmc_space, strength = 2E14): # isotropic source
    """a gamma OpenMC Source for Ta target hit by 25MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (2E14 for 80KW, 25MeV proton beam on Ta)

    
    Returns
    -------
    openmc.Source (openmc.SourceBase object)
        Energy distribution of photons on source site.

    """
    # from file: G:\gammas\gamma_25MeV_Ta_L1_r015.m
    # protons 25 MeV on cylindrical Ta target, L= 1.0 mm, r= 0.15 mm
    Gammas_per_Proton =  0.017206264496000004  # twice the particles of half the angular range
    Neutrons_per_Proton = 0.0110809 # should be calculated on a larger target
    Neutrons_per_Proton = 0.0110034 # computation 25MeV_Ta_r3.m
    gamma_source_strength = strength * Gammas_per_Proton / Neutrons_per_Proton
    erg_bins = [100000.0, 125893.0, 158489.0, 199526.0, 251189.0, 316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0]
    erg_distrib = [0.2912, 0.0452, 0.0758, 0.187, 0.0561, 0.095, 0.0673, 0.0436, 0.025, 0.0345, 0.0255, 0.0169, 0.0122, 0.0111, 0.0087, 0.0038, 0.001, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0]
    energy = openmc.stats.Tabular(erg_bins, erg_distrib, interpolation='histogram')
    return openmc.Source(space= openmc_space, energy= energy, strength= gamma_source_strength, particle='photon')


def gamma_sourceTa40(openmc_space, strength = 5.25E14): # isotropic source
    """a gamma OpenMC Source for Ta target hit by 40MeV protons


    Parameters
    ----------
    openmc_space :  openmc.stats.Spatial
        Spatial Distributions of neutron produced in proton target,
        for instance openmc.stats.Box((xmin, ymin, zmin), (xmax, ymax, zmax))
        or openmc.stats.Point((0., 0., 0.))
    strength : float, optional
        Number of fast NEUTRONS produced on target
        (5.25E14 for 80KW, 40MeV proton beam on Ta)

    
    Returns
    -------
    openmc.Source (openmc.SourceBase object)
        Energy distribution of photons on source site.

    """
    # from file: G:\gammas\gamma_40MeV_Ta_L2_r03.m
    # protons 40 MeV on cylindrical Ta target, L= 2.1 mm, r= 0.3 mm
    Gammas_per_Proton =  0.04403489378  # twice the particles of half the angular range
    Neutrons_per_Proton = 0.0419996 # must be calculated on a larger target
    Neutrons_per_Proton = 0.042238770808 # computation 40MeV_Ta_r3.m
    gamma_source_strength = strength * Gammas_per_Proton / Neutrons_per_Proton
    erg_bins = [100000.0, 125893.0, 158489.0, 199526.0, 251189.0, 316228.0, 398107.0, 501187.0, 630957.0, 794328.0, 1000000.0, 1258930.0, 1584890.0, 1995260.0, 2511890.0, 3162280.0, 3981070.0, 5011870.0, 6309570.0, 7943280.0, 10000000.0, 12589300.0, 15848900.0, 19952600.0, 25118900.0, 31622800.0]
    erg_distrib = [0.168, 0.0512, 0.088, 0.2089, 0.1029, 0.1028, 0.0776, 0.0431, 0.0332, 0.0388, 0.0261, 0.0179, 0.0131, 0.0103, 0.0087, 0.0055, 0.0032, 0.0007, 0.0001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0]
    energy = openmc.stats.Tabular(erg_bins, erg_distrib, interpolation='histogram')
    return openmc.Source(space= openmc_space, energy= energy, strength= gamma_source_strength, particle='photon')

def source_run_test(test_source = sourceBe40 ):
    materials = openmc.Materials([]) 
    
    # geometry
    world_limit= openmc.Sphere(r= 5, boundary_type='vacuum')
    world  = openmc.Cell(region= -world_limit) 
#    world  = openmc.Cell(1, name="world", region= -world_limit) 
    geometry = openmc.Geometry([world])
    
    source = test_source(openmc.stats.Point((0., 0., 0.)))
    
    # tallies
    surface_filter = openmc.SurfaceFilter(bins = [world_limit])
    energy_bins= np.logspace(4, 8, 41)   # 10 pts par decade de 10Kev a 100MeV
    energy_filter= openmc.EnergyFilter(energy_bins)
    cos_bins= np.array([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 
         0.0,   0.1,  0.2,  0.3,  0.4,   0.5,  0.6,  0.7,  0.8, 0.9,  1.0])
    angle_bins= np.arccos(-cos_bins) # angles croissants
    angle_filter = openmc.PolarFilter(angle_bins)
    mix_Tally= openmc.Tally(name= "mixte")
    mix_Tally.filters = [energy_filter, angle_filter]
    mix_Tally.scores = ['flux']
    tallies = openmc.Tallies([mix_Tally])
    
    # settings
    settings = openmc.Settings(source = source, run_mode = 'fixed source', batches = 10)
    settings.particles = int(1e6)
    
    model = openmc.Model(geometry, materials, settings, tallies)
    
    sp_filename = model.run()
    with openmc.StatePoint(sp_filename) as sp:
        tally= sp.get_tally(name="mixte" )
        # my_frame = tally.get_pandas_dataframe()
        my_array= tally.get_reshaped_data().squeeze()  
    # mf= my_frame.pivot(index ="polar low [rad]", columns ="energy low [eV]", values="mean") 
    # data_0 =np.array(mf) # first method
    # print(data_0.shape)  # : (20, 40)
    # data_1= np.array(my_frame["mean"]) # second method
    # data_1= data_1.reshape(40,20).transpose()   
    data= my_array.transpose() # third method
    # print(data.shape)  # : (20, 40)
    return data, test_source.__name__

if __name__ == "__main__" :
    import matplotlib.pyplot as plt
    
    # get data
    data, fn_name = source_run_test()
    
    # plot data
    plt.hot()
    axe= plt.gca()
    axe.set_yticks([1,0.5,0,-0.5,-1])
    axe.set_yticklabels([1,0.5,0,-0.5,-1])
    axe.set_xticks([0, 5, 10, 15, 20, 25, 30, 35, 40])
    axe.set_xticklabels([0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100])
    axe.set_xlabel("Energy (MeV)")
    axe.set_ylabel("cos")
    plt.imshow(data, extent=[0,40,-1,1,], aspect= 'auto')
    plt.title(fn_name)
    plt.colorbar()
