# Processing Surface_Source data
# as written in "surface_source.h5"
# when using the function 
#     >settings.surf_source_write=dict(surface_ids= [planeE.id], max_particles= 100000000)  
# Available functions
#  > particles=read_surface_source("surface_source.h5")  , default filename
#  > N_flux=get_flux(particles,0.1,5) , neutrons emitted with E<0.1 and angle wrt Oz < 5°
    
import numpy as np
import h5py

pos_dtype = np.dtype([('x', '<f8'), ('y', '<f8'), ('z', '<f8')])
source_dtype = np.dtype([
        ('r', pos_dtype),
        ('u', pos_dtype),
        ('E', '<f8'),
        ('time', '<f8'),
        ('wgt', '<f8'),
        ('delayed_group', '<i4'),
        ('surf_id', '<i4'),
        ('particle', '<i4'),
    ])

# filename = "surface_source.h5" # non par défaut du fichier source

def read_surface_source(filename="surface_source.h5"):
    with h5py.File(filename, "r") as f:
        particles= np.array(f["source_bank"][()], dtype=source_dtype)
    return particles
   
def is_fast(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return e > 0.1
def is_thermal(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return e < 0.1
def is_thermal_up(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return (e < 0.1) and (u[2]>0)
def is_thermal_down(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return (e < 0.1) and (u[2]<0)    
def is_cold(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return e < 0.005
def selectionX(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return r[0]
def selectionY(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return r[1]
def is_thermal_in5deg(ruetwdsp):
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return (e < 0.1) and (u[2] >0.9962)  
def is_emitted_in_angle(ruetwdsp,Emin,Emax,angle): # E is the max energy, angle is the max angle wrt (Oz)
    (r,u,e,t,w,d,s,p) = ruetwdsp
    return (e>Emin) and (e < Emax) and (u[2] > np.cos(angle*np.pi/180))  

def get_fast(particles):
    N_fast= np.fromiter( (ruetwdsp for ruetwdsp in particles if is_fast(ruetwdsp)), dtype=source_dtype)
    return N_fast

def get_thermal(particles):
    N_thermal= np.fromiter( (ruetwdsp for ruetwdsp in particles if is_thermal(ruetwdsp)), dtype=source_dtype)
    return N_thermal

def get_thermal_up(particles):
    N_thermal_up= np.fromiter( (ruetwdsp for ruetwdsp in particles if is_thermal_up(ruetwdsp)), dtype=source_dtype)
    return N_thermal_up

def get_thermal_down(particles):
    N_thermal_down= np.fromiter( (ruetwdsp for ruetwdsp in particles if is_thermal_down(ruetwdsp)), dtype=source_dtype)
    return N_thermal_down

def get_thermal_5deg(particles):
    N_thermal_5deg= np.fromiter( (ruetwdsp for ruetwdsp in particles if is_thermal_in5deg(ruetwdsp)), dtype=source_dtype)
    return N_thermal_5deg

def get_cold(particles):
    N_cold= np.fromiter( (ruetwdsp for ruetwdsp in particles if is_cold(ruetwdsp)), dtype=source_dtype)
    return N_cold

# neutrons with an energy below E and emitted within an angular range <angle in the z direction 
def get_flux(particles, Emin=0, Emax=0.1, angle = 5):
    N_flux= np.fromiter( (ruetwdsp for ruetwdsp in particles if is_emitted_in_angle(ruetwdsp,Emin,Emax,angle)), dtype=source_dtype)
    return N_flux
    
# posX= np.fromiter( (selectionX(ruetwdsp) for ruetwdsp in N_cold ), dtype= "float") #'<f8')
# posY= np.fromiter( (selectionY(ruetwdsp) for ruetwdsp in N_cold ), dtype= "float") #'<f8')

# binsX = np.sin((np.pi/180) * np.linspace(-30, 30, num= 61, endpoint=True))
# binsY= np.sin((np.pi/180)* np.linspace(-30, 30, num= 61, endpoint=True))
# XY, xedges, yedges= np.histogram2d(posX,posY, 
#                                   range=((-0.3,0.3),(-0.2,0.2)),
#                                   bins= (24,12))
                                   # bins= (binsX,binsY)
                                   #)
# XY=XY.T # transpose
# central= XY[41:48,41:48]
# print(xedges)
# print(f"{filename}, {particles.size} N_sortie, {N_cold.size} N_froids, {central.sum():.0f} in 7 msr")
# plt.imshow(XY,extent=[-30,30,-30,30])

# print(f"{filename}, {particles.size} N_total, {N_fast.size} N_fast (E>100meV), {N_thermal.size} N_thermal (E<100meV), {N_thermal_up.size} N_thermal_up (E<100meV), {N_thermal_down.size} N_thermal_down (E<100meV)")