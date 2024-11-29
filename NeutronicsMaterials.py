#!/usr/bin/env python
# coding: utf-8

# Version 1 : July 12th 2024 : Note that the materials are not depletable by default

# # Prerequisite
# * install NeutronicsMaterialMaker : conda install -c conda-forge neutronics_material_maker
# * If conda does not work, try [pip install coolprop],
#   then conda install -c conda-forge neutronics_material_maker or pip install neutronics-material-maker
#   + Cross your fingers it did not break conda...
# * Compiled with 

# # Material list 
# 
# #### Copper alloys:(http://uddeholm.gr/Storage/Media/Shared/SteelBrochures/Moldmax%20HH/moldmax_xl-english.pdf)
# <ul>
# <li>Moldmax XL 
# 
#     Cu 75%, Ni 9%, Sn 6%
#     density = 8.9 g/cm3 at 300K
# </ul>
# 
# #### Stainless steels:(https://alloysintl.com/inventory/stainless-steel-supplier)
# <ul>
# <li>SS440
# 
#     Fe 78.4 – 83.4%, Cr 16.0 – 18.0%, Mn ≤ 1.0%, Si ≤ 1.0%, Mo ≤ 0.75%, C ≤ 0.60 – 0.75%, P ≤ 0.04%, S ≤ 0.03%
#     density = 7.80 g/cm3
# 
# <li>SS304
# 
#     Fe 71.00%, Cr 19.00%, Ni 9.0%, Mn ≤ 2.0%, Si ≤ 0.75%, C ≤0.080%, P ≤ 0.045%, S ≤ 0.03%
#     density = 8.03 g/cm3
# 
# <li>SS304L
# 
#     Fe balance, Cr 18.00 – 20.00%, Ni 8.00 – 12.00%, Mn ≤ 2.0%, Si ≤ 0.75%, N ≤0.10%, C ≤0.03%, P ≤ 0.045%, S ≤ 0.03%
#     density = 8.03 g/cm3
# 
# <li>SS316
# 
#     Fe balance, Cr 16.00 – 18.00%, Ni 10.00 – 14.00%, Mo 2.00 – 3.00%, Mn ≤ 2.0%, Si ≤ 0.75%, N ≤0.10%, C ≤0.03%, P ≤ 0.045%, S ≤ 0.03%
#     density = 7.99 g/cm3
# 
# <li>SS316L (same as SS316)
# 
#     Fe balance, Cr 16.00 – 18.00%, Ni 10.00 – 14.00%, Mo 2.00 – 3.00%, Mn ≤ 2.0%, Si ≤ 0.75%, N ≤0.10%, C ≤0.03%, P ≤ 0.045%, S ≤ 0.03%
#     density = 7.99 g/cm3
# </ul>
# 
# #### Aluminum alloys (https://alloysintl.com/fr/inventory/aluminum-alloys-supplier)
# <ul>
# <li>Al5086
# 
#      Al 93.0 - 96.3%, Mg 3.5 - 4.5%, Mn ≤ 0.2 - 0.7%, Fe ≤ 0.50%, Si ≤ 0.40%, Cr ≤ 0.25%, Zn ≤ 0.25%, Ti ≤ 0.15%, Cu ≤ 0.1%
#      density = 2,66 g/cm3
# 
# </ul>
# 
# #### AlBeMet (https://www.materion.com/en/products/performance-materials/metal-matrix-composites/albemet-albecast)
# 
#     Al balance, Be 60.00 - 64.00%, O 1.00%, C 0.1%, other metals, each 0.2%
#     density = 2.071 - 2.122
# 
# #### Mirrobor (https://mirrotron.com/en/products/radiation-shielding)
# 
#     B4C ≥ 80%, (20% 10B; 80% 11B), glue 20% (C 70%, O 25%, H 5%), 
# 
# #### Concretes (S.J. Park, 2014)
# <ul>
#     <li> Inner layer
#         
#         Ordinary concrete (H 0.5568%, O 49.892%, Na 1.71623%, Mg 0.2592%, Al 4.5849%, Si 31.55%, K 1.9181%, Ca 8.2920%, Fe 1.2308%) 50%, polyethylene (H 14.37%, C 85.63%) 50%
# <li> Outer layer
#         
#         Ordinary concrete 98%, B4C 2%
#     
# </ul>
# 
# 
# #### Lead (https://www.azom.com/article.aspx?ArticleID=9514)
# <ul>
# <li>  Lead-Calcium (PbCa) Alloy
#         
#     Pb 99.85-99.97%, Ca 0.03 to 0.15%
#     density = 11.34g/cm3
# 
# <li> Hard Lead (96Pb-4Sb), UNS L52901, Cold-Rolled (https://www.matweb.com/search/datasheet.aspx?matguid=0a27d89051e24ff1a97eff4e295803cd&ckck=1)
# 
#     Pb 96%, Sb 4%
#     density = 11.04 g/cm3
# 
# <li> Lead-Tin alloy
# 
#     Pb 96%, Sn 4%
# 
#     
# </ul>

import openmc
import neutronics_material_maker as nmm

all_materials = nmm.AvailableMaterials()

def MatinList(material):
    return material in all_materials

def LookFor(string):
    for i in all_materials:
        i_lower = i.lower()
        if string.lower() in i_lower:
            print(i)

def addElem(element):
    if element in all_materials:
        return nmm.Material.from_library(element).openmc_material
    else:
        print(f"the element '{element}' is not in the list, use LookFor() to help")

def addMat(material):
    if material in all_materials:
        return nmm.Material.from_library(material, temperature=300, pressure= 1.3e5).openmc_material
    else:
        print(f"the element '{material}' is not in the list, use LookFor() to help")
        
############# Materials ##############
################################### Elements definition #########################################
Al = addMat("Aluminum")
Cu = addMat("Copper")
Be = addMat("Beryllium")
Tl = addMat("Tantalum")
Al = addMat("Aluminum")
O = addMat("Oxygen")
Cr = addMat("Chromium")
Au = addMat("Gold")
W = addMat("Tungsten")
Mo = addMat("Molybdenum")
Hg = addMat("Mercury")
Na = addMat("Sodium")
Mg = addMat ("Magnesium")
Si = addMat ("Silicon")
Fe = addMat ("Iron")
H = addMat ("Hydrogen")
B = addMat ("Boron")
Sn = addMat ("Tin")
Pb = addMat("Lead")

Mn = openmc.Material(name='Mn')
Mn.add_element('Mn',1.,'ao')
Mn.set_density('g/cm3',7.26)

C = openmc.Material(name='C')
C.add_element('C',1.,'ao')
C.set_density('g/cm3',2.2)

Co = openmc.Material(name='Co')
Co.add_element('Co',1.,'ao')
Co.set_density('g/cm3',8.90)

K = openmc.Material(name='Potassium')
K.add_element('K',1.,'ao')
K.set_density('g/cm3',0.89)

Ca = openmc.Material(name='Calcium')
Ca.add_element('Ca',1.,'ao')
Ca.set_density('g/cm3',1.55)

Sb = openmc.Material(name='Antimony')
Sb.add_element('Sb',1.,'ao')
Sb.set_density('g/cm3',6.68)

##################################################################################

water = addMat("H2O")

Al_5086_O = addMat("Aluminum, alloy 5086-O")

Stainless_steel_440A = addMat("Steel, Stainless 440A")
Stainless_steel_304 = addMat("Steel, Stainless 304")
Stainless_steel_304L = addMat("Steel, Stainless 304L")
Stainless_steel_316 = addMat("Steel, Stainless 316")
Stainless_steel_316L = addMat("Steel, Stainless 316L")

Moldmax_XL = openmc.Material(name = "Moldmax XL") 
Moldmax_XL.set_density('g/cm3', 8.9)
Moldmax_XL.add_element('Ni' , 9. , 'wo')
Moldmax_XL.add_element('Sn' , 6. , 'wo')
Moldmax_XL.add_element('Cu' , 75. , 'wo')

AlBeMet = openmc.Material.mix_materials([Be,Al,O, C ,Mn,Cr,Tl,Au, W, Mo, Hg, Co],
                                        [62/100, 37/100, 0.2/100, 0.1/100, 0.0875/100, 0.0875/100, 0.0875/100, 0.0875/100,0.0875/100,0.0875/100,0.0875/100,0.0875/100], 
                                        "wo", name= 'AlBeMet')
AlBeMet.set_density('g/cm3',2.1)

Ordinary_concrete = openmc.Material.mix_materials([H, O, Na, Mg, Al, Si, K, Ca, Fe],[0.5568/100, 49.892/100, 1.71623/100, 0.2592/100, 4.58488/100, 31.55/100, 1.91807/100, 8.29198/100, 1.23084/100], "wo", name= 'Ordinary concrete')
Boron_carbide = openmc.Material.mix_materials([B, C],[4/5, 1/5], "ao", name= 'Boron carbide')

Polyethylene = addMat("Polyethylene, Non-borated")

Concrete_PE = openmc.Material.mix_materials([Ordinary_concrete, Polyethylene],[50/100, 50/100], "wo", name= 'Concrete inner layer')
Concrete_B4C = openmc.Material.mix_materials([Ordinary_concrete, Boron_carbide],[98/100, 2/100], "wo", name= 'Concrete outer layer')

glue = openmc.Material.mix_materials([H, C, O],[5/100, 70/100, 25/100], "wo", name= 'glue')
Mirrobor = openmc.Material.mix_materials([Boron_carbide, glue],[80/100, 20/100], "wo", name= 'Mirrobor')
Mirrobor.set_density('g/cm3',1.55)

Lead_Tin = openmc.Material.mix_materials([Pb, Sn],[96/100, 4/100], "wo", name= 'Lead Tin')
Lead_Tin.set_density('sum') # density = 11.10 g/cm3
Lead_Antimony = openmc.Material.mix_materials([Pb, Sb],[96/100, 4/100], "wo", name= 'Lead Antimony')
Lead_Antimony.set_density('g/cm3',11.04)
Lead_Calcium = openmc.Material.mix_materials([Pb, Ca],[99.85/100, 0.15/100], "wo", name= 'Lead Calcium')
Lead_Calcium.set_density('g/cm3',11.34)


# EXEMPLES D'UTILISATION

# print(Moldmax_XL)
# print(Boron_carbide)
# print(Polyethylene)
# print(Lead_Tin)

# all_materials = nmm.AvailableMaterials()
# print(all_materials.keys())

# LookFor("stainless")
