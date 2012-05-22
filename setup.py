from numpy.distutils.core import setup

import sys, os

version = '1.0'

def configuration ( parent_package='', top_path=None ):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(parent_package,top_path, )
    
    config.add_extension ('lib_sixs_mcrm', 
    sources = [ "sixs/lib_sixs_mcrm.pyf", \
        "sixs/AATSR.f", "sixs/ABSTRA.f", \
        "sixs/AEROPROF.f", "sixs/AEROSO.f", \
        "sixs/AKTOOL.f", "sixs/ALI.f", \
        "sixs/ASTER.f", "sixs/ATMREF.f", \
        "sixs/AVHRR.f", "sixs/BBM.f", \
        "sixs/BDM.f", "sixs/BRDFGRID.f", \
        "sixs/CHAND.f", "sixs/CLEARW.f", \
        "sixs/CSALBR.f", "sixs/DICA1.f", \
        "sixs/DICA2.f", "sixs/DICA3.f", \
        "sixs/DISCOM.f", "sixs/DISCRE.f", \
        "sixs/DUST.f", "sixs/ENVIRO.f", \
        "sixs/EQUIVWL.f", "sixs/ETM.f", \
        "sixs/GAUSS.f", "sixs/GLI.f", \
        "sixs/GOES.f", "sixs/HAPKALBE.f", \
        "sixs/HAPKBRDF.f", "sixs/HRV.f", \
        "sixs/HYPBLUE.f", "sixs/IAPIALBE.f", \
        "sixs/IAPIBRDF.f", "sixs/IAPITOOLS.f", \
        "sixs/INTERP.f", "sixs/ISO.f", \
        "sixs/KERNEL.f", "sixs/KERNELPOL.f", \
        "sixs/LAKEW.f", \
        "sixs/main_ssssss.f", "sixs/MAS.f", \
        "sixs/MERIS.f", "sixs/METEO.f", \
        "sixs/METH1.f", "sixs/METH2.f", \
        "sixs/METH3.f", "sixs/METH4.f", \
        "sixs/METH5.f", "sixs/METH6.f", \
        "sixs/MIDSUM.f", "sixs/MIDWIN.f", \
        "sixs/MIE.f", "sixs/MINNALBE.f", \
        "sixs/MINNBRDF.f", "sixs/MOCA1.f", \
        "sixs/MOCA2.f", "sixs/MOCA3.f", \
        "sixs/MOCA4.f", "sixs/MOCA5.f", \
        "sixs/MOCA6.f", "sixs/MODISALBE.f", \
        "sixs/MODISBRDF.f", "sixs/MODIS.f", \
        "sixs/MSS.f", "sixs/NIOX1.f", \
        "sixs/NIOX2.f", "sixs/NIOX3.f", \
        "sixs/NIOX4.f", "sixs/NIOX5.f", \
        "sixs/NIOX6.f", "sixs/OCEAALBE.f", \
        "sixs/OCEABRDF.f", "sixs/OCEABRDFFAST.f", \
        "sixs/OCEA.f", "sixs/OCEATOOLS.f", \
        "sixs/ODA550.f", "sixs/ODRAYL.f", \
        "sixs/OS.f", "sixs/OSPOL.f", \
        "sixs/OXYG3.f", "sixs/OXYG4.f", \
        "sixs/OXYG5.f", "sixs/OXYG6.f", \
        "sixs/OZON1.f", "sixs/PLANPOL.f", \
        "sixs/POLDER.f", "sixs/POLGLIT.f", \
        "sixs/POLNAD.f", "sixs/POSGE.f", \
        "sixs/POSGW.f", "sixs/POSLAN.f", \
        "sixs/POSMTO.f", "sixs/POSNOA.f", \
        "sixs/POSSOL.f", "sixs/POSSPO.f", 
        "sixs/PRESPLANE.f", "sixs/PRESSURE.f", \
        "sixs/PRINT_ERROR.f", "sixs/RAHMALBE.f", \
        "sixs/RAHMBRDF.f", "sixs/ROUJALBE.f", \
        "sixs/ROUJBRDF.f", "sixs/SAND.f", \
        "sixs/SCATRA.f", "sixs/SEAWIFS.f", \
        "sixs/SOLIRR.f", "sixs/SOOT.f", \
        "sixs/SPECINTERP.f", "sixs/SPLIE2.f", \
        "sixs/SPLIN2.f", "sixs/SPLINE.f", \
        "sixs/SPLINT.f", "sixs/STM.f", \
        "sixs/SUBSUM.f", "sixs/SUBWIN.f", \
        "sixs/TM.f", "sixs/TROPIC.f", \
        "sixs/TRUNCA.f", "sixs/US62.f", \
        "sixs/VARSOL.f", "sixs/VEGETA.f", \
        "sixs/VERSALBE.f", "sixs/VERSBRDF.f", \
        "sixs/VERSTOOLS.f", "sixs/VGT.f", \
        "sixs/VIIRS.f", "sixs/WALTALBE.f", \
        "sixs/WALTBRDF.f", "sixs/WATE.f", \
        "sixs/WAVA1.f", "sixs/WAVA2.f", \
        "sixs/WAVA3.f","sixs/WAVA4.f", \
        "sixs/WAVA5.f","sixs/WAVA6.f", "sixs/sixs_mcrm_sim.f90"])
    return config

if __name__ == "__main__":    
    # This is a hack, as F77/F90 flags can be passed in the config object
    # but only on recent versions of numpy/f2py
    sys.argv.extend ( ["config_fc", "--fcompiler=gnu95", 
#            "--f90exec=/usr/bin/gfortran44", 
            "--f77flags='-ffixed-form -ffixed-line-length-none'" ])

    DISTNAME = 'sixs'
    DESCRIPTION = '6s Python wrappers'
    LONG_DESCRIPTION = open('README.rst').read()
    MAINTAINER = 'Jose Gomez-Dans/NCEO & University College London'
    MAINTAINER_EMAIL = "j.gomez-dans@ucl.ac.uk"
    URL = 'http://6s.ltdri.com/'
    LICENSE = 'Undecided'
    VERSION = "1.0.2"
    DOWNLOAD_URL="https://github.com/jgomezdans/sixs/zipball/master"
    setup ( configuration = configuration,
    name=DISTNAME,
    maintainer=MAINTAINER,
    include_package_data=True,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    zip_safe=False, # the package can run out of an .egg file
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: Fortran',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS'
        ], packages=["sixs"]
        )
            
            
