#!/usr/bin/env python3
import sys
import random
import json
r = lambda: random.randint(0,255)
labels_list = "building;edifice sky floor;flooring tree ceiling road;route bed windowpane;window grass cabinet sidewalk;pavement person;individual;someone;somebody;mortal;soul earth;ground door;double;door table mountain;mount plant;flora;plant;life curtain;drape;drapery;mantle;pall chair car;auto;automobile;machine;motorcar water painting;picture sofa;couch;lounge shelf house sea mirror rug;carpet;carpeting field armchair seat fence;fencing desk rock;stone wardrobe;closet;press lamp bathtub;bathing;tub;bath;tub railing;rail cushion base;pedestal;stand box column;pillar signboard;sign chest;of;drawers;chest;bureau;dresser counter sand sink skyscraper fireplace;hearth;open;fireplace refrigerator;icebox grandstand;covered;stand path stairs;steps runway case;display;case;showcase;vitrine pool;table;billiard;table;snooker;table pillow screen;door;screen stairway;staircase river bridge;span bookcase blind;screen coffee;table;cocktail;table toilet;can;commode;crapper;pot;potty;stool;throne flower book hill bench countertop stove;kitchen;stove;range;kitchen;range;cooking;stove palm;palm;tree kitchen;island computer;computing;machine;computing;device;data;processor;electronic;computer;information;processing;system swivel;chair boat bar arcade;machine hovel;hut;hutch;shack;shanty bus;autobus;coach;charabanc;double-decker;jitney;motorbus;motorcoach;omnibus;passenger;vehicle towel light;light;source truck;motortruck tower chandelier;pendant;pendent awning;sunshade;sunblind streetlight;street;lamp booth;cubicle;stall;kiosk television;television;receiver;television;set;tv;tv;set;idiot;box;boob;tube;telly;goggle;box airplane;aeroplane;plane dirt;track apparel;wearing;apparel;dress;clothes pole land;ground;soil bannister;banister;balustrade;balusters;handrail escalator;moving;staircase;moving;stairway ottoman;pouf;pouffe;puff;hassock bottle buffet;counter;sideboard poster;posting;placard;notice;bill;card stage van ship fountain conveyer;belt;conveyor;belt;conveyer;conveyor;transporter canopy washer;automatic;washer;washing;machine plaything;toy swimming;pool;swimming;bath;natatorium stool barrel;cask basket;handbasket waterfall;falls tent;collapsible;shelter bag minibike;motorbike cradle oven ball food;solid;food step;stair tank;storage;tank trade;name;brand;name;brand;marque microwave;microwave;oven pot;flowerpot animal;animate;being;beast;brute;creature;fauna bicycle;bike;wheel;cycle lake dishwasher;dish;washer;dishwashing;machine screen;silver;screen;projection;screen blanket;cover sculpture hood;exhaust;hood sconce vase traffic;light;traffic;signal;stoplight tray ashcan;trash;can;garbage;can;wastebin;ash;bin;ash-bin;ashbin;dustbin;trash;barrel;trash;bin fan pier;wharf;wharfage;dock crt;screen plate monitor;monitoring;device bulletin;board;notice;board shower radiator glass;drinking;glass clock"

labels = labels_list.split(" ")

class Label:
    def __init__(self, index, id, name):
        self.id = str(index)
        self.name = name
        self.color = '#%02X%02X%02XFF' % (r(),r(),r())
        self.is_empty = id == 0
        self.parent_id = ""

#labels[0]
print('#%02X%02X%02XFF' % (r(),r(),r()))

label = labels[0]

output_labels = []
for index, label in enumerate(labels):
    output_labels.append(vars(Label(index, index, label)))

print(json.dumps(output_labels))
