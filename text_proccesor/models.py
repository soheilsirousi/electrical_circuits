from electrical.models import Mesh

class Sentence:

    #(-V1+=12)>(R1=10)>(R2=30)>(V2=12) | A = ?

    def space(self, sentence):
        return sentence.split('\n')[0]

    def arrow(self, sentence):
        return sentence.split('>')

    def equal(self, object):
        return object[1:len(object) - 1].split('=')

    def sign(self, key, value):
        if key[0].upper() == 'R':
            return key, float(value)
        if key[0] == '-':
            return key[1:len(key) - 1], float(value)
        if key[0] == '+':
            return key[1:len(key) - 1], -1 * float(value)

    def to_mesh(self, sentence):
        mesh = Mesh()
        sentence = self.space(sentence)
        objects = self.arrow(sentence)

        for object in objects:
            key, value = self.equal(object)
            key, value = self.sign(key, value)
            if key[0].upper() == 'V':
                mesh.VoltageSources = {int(key[1:]): value}
            elif key[0].upper() == 'R':
                mesh.Resistances = {int(key[1:]): value}
            else:
                raise ValueError('Unknown key {}'.format(key[0]))

        return mesh


if __name__ == '__main__':
    sen = Sentence()
    sen.to_mesh('(-V1+=12)>(R1=10)>(R2=30)>(+V2-=12)')