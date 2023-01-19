from ase.io.vasp import write_vasp
from ase.spacegroup import crystal
import yaml

def conv_float(dict1):
    for k, v in dict1.items():
        dict1[k] = float(v)
    return dict1

if __name__ == '__main__':
    with open('rendered_wano.yml') as file:
        wano_file = yaml.full_load(file)

    wano_file = conv_float(wano_file)


    a = float(wano_file['a'])
    c = float(wano_file['c'])

    Graphite_basis = [(0.00000000,  0.00000000,  0.25000000), (0.00000000,  0.00000000,  0.75000000),
    (0.33333333,  0.66666667,  0.25000000), (0.66666667,  0.33333333,  0.75000000)]

    #spacegroup=194=P63/mmc

    Graphite_AB = crystal(['C', 'C', 'C', 'C'], Graphite_basis, spacegroup=194,
                cellpar=[a, a, c, 90, 90, 120])

    write_vasp('POSCAR', Graphite_AB, direct=True, label='Graphite')

    with open("graphite_results.yml",'w') as out:
        yaml.dump(wano_file, out,default_flow_style=False)