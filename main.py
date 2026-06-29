import numpy as np
import config as con
import Hamiltonians.hubbard as hub 
import Basis_operations.basis as bs
import Basis_operations.binary as bi
import Basis_operations.com as com
import Hamiltonians.ext_hubbard as ex
import Hamiltonians.ppp as p 
import Huckel.huckel_main as hu

run = input("Which Model Hamiltonian Would you like to Use(Huckel(hu)/Hubbard(hr)/Extended Hubbard(ehr)/PPP(p):)")

match run:
    case "hu":
        con.hu()
        hu.hu_main()
    case "hr":
        con.hr()
        hub.main_hub()
    case "ehr":
        con.ehr()
        ex.main_ext()
    case "p":
        con.p()
        p.main_ppp()