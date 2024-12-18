from electrical.models import Mesh

class Sentence:

    #(V1=12)>(R1=10)>(R2=30)>(V2=12) | A = ?

    @classmethod
    def text_to_mesh(cls, sentence):
        mesh = Mesh()
        objects = sentence.split('\n')[0]
        objects = objects.split('>')
        for object in objects:
            key, value = object[1:len(object) - 1].split('=')
            if key[0].upper() == 'V':
                mesh.VoltageSources = {int(key[1:]) : float(value)}
            elif key[0].upper() == 'R':
                mesh.Resistances = {int(key[1:]) : float(value)}
            else:
                raise ValueError('Unknown key {}'.format(key[0]))

        return mesh

