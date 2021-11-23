#!/bin/bash

nohup python3 -u generate_images.py "/home/tomoe/mc/bench/test[0-9].root" > nohup1.out &
nohup python3 -u generate_images.py /home/tomoe/mc/bench/test_1500MeV.root > nohup2.out &
nohup python3 -u generate_images.py /home/tomoe/mc/bench/test_1700MeV.root > nohup3.out &
nohup python3 -u generate_images.py /home/tomoe/mc/bench/test_2000MeV.root > nohup4.out &