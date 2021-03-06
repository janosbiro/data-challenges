import pandas as pd
import json

input_json = json.load(open('input.json','r'))
data_args = json.load(open('data.json','r'))

df = pd.read_pickle(data_args['staging_folder'] + '/filtered.pickle')

out = []

for place in input_json:
    
    df['distance'] = ((place['lon']-df['lon']) ** 2 + (place['lat']-df['lat']) ** 2)
    
    out.append(df.ix[df['distance'].idxmin(),["lon","lat","name"]].to_dict().copy())

json.dump(out,open('output.json','w'))
