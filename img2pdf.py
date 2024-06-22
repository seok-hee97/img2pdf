import os
import img2pdf

def makePDF(path):
    '''
    path : dir path
    '''
    # for check the path
    if not os.path.exists(path):
        print("Input the right path")
        return 1
    

    dirname = os.path.dirname(path)
    print(dirname)
    filename = dirname + ".pdf"
    
    # make PDF file and write    
    with open(filename, "wb") as file:
        file.write(img2pdf.convert([i for i in os.listdir(path) if i.endswith(".png")]))
        
        
        
        
if __name__ == "__main__":
    test_path = "/Users/jangseokhee/workspace/devops/image2pdf/초거대-AI의-위험서"
    makePDF(test_path)