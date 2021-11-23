import base64
import glob
import os

def get_base64_image_tag(image_path, mime_type):
    with open(image_path, "rb") as f:
        src = base64.b64encode(f.read()).decode('utf-8')
        return f'''<img src="data:image/{mime_type};base64,{src}" />'''

def write_to_html(file_path="/home/hamada/b4ex/mc/analysis/img_tracks/test_1500MeV.root/png/"):
    mine_type = file_path.split('/')[-2]
    image_path_es = glob.glob('{0}*{1}'.format(file_path, mine_type))
    
    with open(file_path + 'preview.html', 'w') as f:
        for image_path in image_path_es:
            writing_str = get_base64_image_tag(image_path, mine_type)
            f.write(writing_str)
        
def main():
    img_tracks_path = "/home/hamada/b4ex/mc/analysis/img_tracks/"
    target_dir_s = os.listdir(img_tracks_path)
    mine_type_s = ['png/', 'gif/']
    
    for mine_type in mine_type_s:
        for target_dir in target_dir_s:
            write_to_html(img_tracks_path + target_dir + '/' + mine_type)
            print(img_tracks_path + target_dir + '/' + mine_type)
    
if __name__ == '__main__':
    main()