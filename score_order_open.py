import os
import fnmatch
import glob
import pprint
import json

##### To do: create dictionary that defines score order,



#for file in glob.glob("clarinet"):
    #print(file)

#for filename in os.listdir(directory):
        #print(filename)



#/Users/drakedomingue/Desktop/Part PDFs/Lizzie and Lucy PARTS/Lizzie and Lucy PDF Parts/Lizzie and Lucy  - Trombone 1.pdf

#substring_in_list = any(horn in part_pdf for part_pdf in horn)




# Defines score order

#Concert Band Score Order JSON

cb_so_json = {
    "woodwinds": [
      {
        "flute":["piccolo",
                "flute 1",
                "flute 2",
                "flute 3",],
        "oboe": ["oboe 1",
                 "oboe 2",],
        "bassoon": ["bassoon 1",
                    "bassoon 2",],
        "clarinet": ["clarinet 1",
                    "clarinet 2",
                    "clarinet 3",
                    "bass clarinet"],
        "saxophone": ["alto saxophone 1",
                      "alto saxophone 2",
                      "tenor saxophone",
                      "baritone saxophone",],
      }
    ],

    "brass": [
      {
        "horn":["horn 1",
                "horn 2",
                "horn 3",
                "horn 4",
                "horn 1_2",
                "horn 3_4"],
        "trumpet": ["trumpet 1",
                 "trumpet 2",],
        "trombone": ["bassoon 1",
                    "bassoon 2",],
        "euphonium": ["euphonium 1",
                    "euphonium 2",
                    "euphonium",],
        "tuba": ["tuba",
                 "tuba 1",
                 "tuba 2"],
      }
    ],


        "percussion": [
          {
            "percussion":["percussion 1",
                    "percussion 2",
                    "percussion 3",],
            "timpani": ["timpani"],
            "xylophone": ["bassoon 1",
                        "bassoon 2",],
            "marimba": ["marimba",],
            "bells and chimes": ["bells and chimes",],
          }
        ],
    }

#cb = json.loads(cb_so_json)
print(cb_so_json)
#print(cb_so_json['woodwinds'][0]['oboe'])

#Concert Band Score Order dictionary

cb_score_order = {
  'woodwinds': ['piccolo', 'flute 1', 'flute 2', 'flute 3','oboe 1','oboe 2', 'bassoon',
                'clarinet 1', 'clarinet 2', 'clarinet 3','bass clarinet', 'alto saxophone 1',
                'alto saxophone 2', 'tenor saxophone', 'baritone saxophone'],
  'brass': ['horn', 'trumpet 1', 'trombone 1'],
  'percussion': ['percussion 1', 'percussion 2'],
}

json_object = json.dumps(cb_score_order, indent = 4)



# Creates variable to grab every PDF file in the main directory/sub directories

directory = '/Users/drakedomingue/Desktop/Part PDFs/Lizzie and Lucy PARTS/'
part_pdf = glob.glob(f"{directory}/**/*.pdf", recursive = True)


#Creates list of all PDFS without file path

for part in part_pdf:
    edit_part = [part[106:] for part in part_pdf]

edit_json = json.dumps(edit_part, indent = 4)





#for part in edit_part:
