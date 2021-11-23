import os
import ROOT as r
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import tqdm

class TreeImageGenerator():
    fig = plt.figure(figsize = (8, 8))
    pdg = r.TDatabasePDG()
    chain = float('inf')
    i_entry = float('inf')
    root_file_path = ""
    root_file_name = ""
    img_save_path = ""
    drawable_event_indexs = []
    
    def __init__(self, root_file_path):
        self.root_file_path = root_file_path
        self.chain = r.TChain("tree")
        self.chain.Add(root_file_path)
        self.print_tchain_emelents()
        self.root_file_name = self.root_file_path.split('/')[-1]
        self.img_save_path = "./img_tracks/{0}/".format(self.root_file_name)
        self.make_dir()
        
    def make_dir(self):
        os.makedirs(self.img_save_path + "png/", exist_ok=True)
        os.makedirs(self.img_save_path + "gif/", exist_ok=True)
        
    def print_tchain_emelents(self):
        for element in self.chain.GetListOfFiles():
            print('loaded' + '\t' + element.GetTitle())
        
    def get_entry(self, i):
        self.i_entry = i
        self.chain.GetEntry(self.i_entry)
        
    def search_spesific_event(self):
        print('searching reasonable events')
        for i in tqdm.tqdm(range(self.chain.GetEntries())):
            self.chain.GetEntry(i)
            #if len(self.chain.x) < 4: continue
            flag = (111 in self.chain.particle) or (211 in self.chain.particle) or (-211 in self.chain.particle)
            if not flag: continue
            self.drawable_event_indexs.append(i)
        print('{0}/{1} event was found'.format(len(self.drawable_event_indexs), self.chain.GetEntries()))
    
    def draw_track(self, is_save_gif=False):
        ax = self.fig.add_subplot(111, projection='3d')
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title('{0} #{1}'.format(self.root_file_path, self.i_entry))
        
        tracks = dict()
        for j in range(self.chain.nHit):
            if self.chain.particle[j] in tracks:
                tracks[self.chain.particle[j]].append([self.chain.x[j], self.chain.y[j], self.chain.z[j]])
            else:
                tracks[self.chain.particle[j]] = [np.array([self.chain.x[j], self.chain.y[j], self.chain.z[j]])]
        
        for pdg_code, cordinate in tracks.items():
            particle_name = self.pdg.GetParticle(pdg_code).GetName() if pdg_code < 1000000000 else str(pdg_code)
            x, y, z = np.array(cordinate).T
            #ax.plot(x, y, z, label=particle_name)
            if "pi" in particle_name:
                ax.scatter(x, y, z, marker='*', label=particle_name)
            else:
                ax.scatter(x, y, z, label=particle_name)
        ax.plot(np.zeros(10), np.zeros(10), np.linspace(np.min(self.chain.z), np.max(self.chain.z), 10), label='incident line')
        self.fig.legend()
        self.fig.savefig("{0}png/{1}.png".format(self.img_save_path, self.i_entry))
        
        
        if is_save_gif:
            def graph_init():
                ax.clear()
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.set_zlabel("z")
                ax.set_title('{0} #{1}'.format(self.root_file_path, self.i_entry))
                for pdg_code, cordinate in tracks.items():
                    particle_name = self.pdg.GetParticle(pdg_code).GetName() if pdg_code < 1000000000 else str(pdg_code)
                    x, y, z = np.array(cordinate).T
                    #ax.plot(x, y, z, label=particle_name)
                    if "pi" in particle_name:
                        ax.scatter(x, y, z, marker='*', label=particle_name)
                    else:
                        ax.scatter(x, y, z, label=particle_name)
                ax.plot(np.zeros(10), np.zeros(10), np.linspace(np.min(self.chain.z), np.max(self.chain.z), 10), label='incident line')
                return self.fig,

            def graph_animate(i):
                ax.view_init(elev=30., azim=3.6*i)
                return self.fig,
                
            ani = animation.FuncAnimation(self.fig, graph_animate, init_func=graph_init,frames=100, interval=100, blit=True)
            ani.save("{0}gif/{1}.gif".format(self.img_save_path, self.i_entry), writer="imagemagick",dpi=100)
            
        plt.cla()
        plt.clf()
