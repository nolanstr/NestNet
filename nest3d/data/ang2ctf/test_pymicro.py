import pymicro
from pymicro.crystal.ebsd import OimScan

if __name__ == "__main__":
    file_path = "./A01_XY_100_nm.ang"

    ebsd = OimScan.from_file(file_path)

    import pdb;pdb.set_trace()