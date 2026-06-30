import numpy as np
import config as con
import Hamiltonians.hubbard as hub 
import Basis_operations.basis as bs
import Basis_operations.binary as bi
import Basis_operations.com as com
import Hamiltonians.ext_hubbard as ex
import Hamiltonians.ppp as p 
import Huckel.huckel_main as hu
import diagonalization as di

run = input("Which Model Hamiltonian Would you like to Use(Huckel(hu)/Hubbard(hr)/Extended Hubbard(ehr)/PPP(p):)")

match run:
    case "hu":
        con.hu()
        hu.hu_main()
    case "hr":
        con.hr()
        mat = hub.main_hub()
        va,ve = di.scispa(mat)
        x = input("Print the eigenvectors and eigenvalues(0/1):")
        if x == "1":
            print(va)
            print(ve)
        
    case "ehr":
        con.ehr()
        mat = ex.main_ext()
        va,ve = di.scispa(mat)
        x = input("Print the eigenvectors and eigenvalues(0/1):")
        if x == "1":
            print(va)
            print(ve)
        
    case "p":
        con.p()
        mat = p.main_ppp()
        va,ve = di.scispa(mat)
        x = input("Print the eigenvectors and eigenvalues(0/1):")
        if x == "1":
            print(va)
            print(ve)
        