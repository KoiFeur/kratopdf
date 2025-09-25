from PIL import Image
import os, sys

def main(project_path=""):
    if project_path[-1]!="/":
        project_path += "/"
    try:
        os.mkdir(project_path+"png")
        os.mkdir(project_path+"pdf")
    except KeyboardInterrupt:
        quit()
    except:
        pass
    
    try:
        os.listdir(project_path+"kra/")
    except KeyboardInterrupt:
        quit()
    except:
        raise ValueError("You need to put all your .kra into a folder named kra and give the path where the kra folder is")

    os.system(f'cd {project_path}kra; for f in *.kra ; do krita "$f" --export --export-filename "../png/$f.png" ;done')

    dirs = os.listdir(project_path+"png/")
    print(dirs)
    images = [Image.open(project_path+"png/"+f).convert('RGB') for f in dirs]

    pdf_path = project_path+"pdf/final.pdf"
    images[0].save(pdf_path,"PDF",save_all=True, append_images=images[1:])
    
    
    


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        raise ValueError("Include path : uv run main.py [path to the project]")
    main(sys.argv[1])
