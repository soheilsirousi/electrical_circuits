from electrical.models import Mesh
from text_proccesor.models import Sentence

if __name__ == "__main__":
    sen = '(V1=10)>(R1=10)>(R2=30)'
    mesh = Sentence.text_to_mesh(sen)
    print(mesh.Ammeter())