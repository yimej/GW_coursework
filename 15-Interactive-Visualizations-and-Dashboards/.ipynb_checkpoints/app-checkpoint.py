from flask import Flask
import pandas as pd
app = Flask(__name__)

columns_df = pd.read_csv('metadata_columns.csv')
metadata_df = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')
otu_df = pd.read_csv('belly_button_biodiversity_otu_id.csv')
samples_df = pd.read_csv('belly_button_biodiversity_samples.csv')

otu_df.set_index('otu_id', inplace=True)

sample_metadata_df = metadata_df[['AGE', 'BBTYPE', 'ETHNICITY', 'GENDER', 'LOCATION', 'SAMPLEID']]
sample_metadata_df.set_index('SAMPLEID', drop=False, inplace=True)
sample_metadata_dict = sample_metadata_df.to_dict('records')

wfreq_df = metadata_df[['SAMPLEID', 'WFREQ']]
wfreq_df.set_index('SAMPLEID', inplace=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/names')
def list_of_names():
    names = list(samples_df.columns.values)
    return names    

@app.route('/otu')
def otu_descriptions():
    otu_list = otu_df['lowest_taxonomic_unit_found'].tolist()
    return otu_list

@app.route('/metadata/<sample>')
def metadata_for_sample():
    sample = int(sample[3:])
    sample_metadata = sample_metadata_df.loc[sample].to_dict()
    return(sample_metadata)

@app.route('/wfreq/<sample>')
def wfreq_for_sample():
    sample_wfreq = float(wfreq_df.loc[sample])
    return(sample_wfreq)

@app.route('/samples/<sample>')
def info_for_sample():
    info = samples_df.sort_values(sample, ascending=False)
    info_otu = current['otu_id'].tolist()
    info_values = current[sample].tolist()
    info_dict = {'otu_ids': info_otu, 'sample_values': info_values}
    return(info_dict)

if __name__ == "__main__":
    app.run(debug=True)