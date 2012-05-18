from setuptools import setup, find_packages
import sys, os

version = '1.0'

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('eoldaslib',parent_package,top_path, )
    fflags= '-fdefault-real-8 -ffixed-form' 
    
    config.add_extension ('lib_sixs_mcrm', 
    sources = [ "eoldaslib/sixs_obs/lib_sixs_mcrm.pyf", \
        "eoldaslib/sixs_obs/AATSR.f", "eoldaslib/sixs_obs/ABSTRA.f", \
        "eoldaslib/sixs_obs/AEROPROF.f", "eoldaslib/sixs_obs/AEROSO.f", \
        "eoldaslib/sixs_obs/AKTOOL.f", "eoldaslib/sixs_obs/ALI.f", \
        "eoldaslib/sixs_obs/ASTER.f", "eoldaslib/sixs_obs/ATMREF.f", \
        "eoldaslib/sixs_obs/AVHRR.f", "eoldaslib/sixs_obs/BBM.f", \
        "eoldaslib/sixs_obs/BDM.f", "eoldaslib/sixs_obs/BRDFGRID.f", \
        "eoldaslib/sixs_obs/CHAND.f", "eoldaslib/sixs_obs/CLEARW.f", \
        "eoldaslib/sixs_obs/CSALBR.f", "eoldaslib/sixs_obs/DICA1.f", \
        "eoldaslib/sixs_obs/DICA2.f", "eoldaslib/sixs_obs/DICA3.f", \
        "eoldaslib/sixs_obs/DISCOM.f", "eoldaslib/sixs_obs/DISCRE.f", \
        "eoldaslib/sixs_obs/DUST.f", "eoldaslib/sixs_obs/ENVIRO.f", \
        "eoldaslib/sixs_obs/EQUIVWL.f", "eoldaslib/sixs_obs/ETM.f", \
        "eoldaslib/sixs_obs/GAUSS.f", "eoldaslib/sixs_obs/GLI.f", \
        "eoldaslib/sixs_obs/GOES.f", "eoldaslib/sixs_obs/HAPKALBE.f", \
        "eoldaslib/sixs_obs/HAPKBRDF.f", "eoldaslib/sixs_obs/HRV.f", \
        "eoldaslib/sixs_obs/HYPBLUE.f", "eoldaslib/sixs_obs/IAPIALBE.f", \
        "eoldaslib/sixs_obs/IAPIBRDF.f", "eoldaslib/sixs_obs/IAPITOOLS.f", \
        "eoldaslib/sixs_obs/INTERP.f", "eoldaslib/sixs_obs/ISO.f", \
        "eoldaslib/sixs_obs/KERNEL.f", "eoldaslib/sixs_obs/KERNELPOL.f", \
        "eoldaslib/sixs_obs/LAKEW.f", \
        "eoldaslib/sixs_obs/main_ssssss.f", "eoldaslib/sixs_obs/MAS.f", \
        "eoldaslib/sixs_obs/MERIS.f", "eoldaslib/sixs_obs/METEO.f", \
        "eoldaslib/sixs_obs/METH1.f", "eoldaslib/sixs_obs/METH2.f", \
        "eoldaslib/sixs_obs/METH3.f", "eoldaslib/sixs_obs/METH4.f", \
        "eoldaslib/sixs_obs/METH5.f", "eoldaslib/sixs_obs/METH6.f", \
        "eoldaslib/sixs_obs/MIDSUM.f", "eoldaslib/sixs_obs/MIDWIN.f", \
        "eoldaslib/sixs_obs/MIE.f", "eoldaslib/sixs_obs/MINNALBE.f", \
        "eoldaslib/sixs_obs/MINNBRDF.f", "eoldaslib/sixs_obs/MOCA1.f", \
        "eoldaslib/sixs_obs/MOCA2.f", "eoldaslib/sixs_obs/MOCA3.f", \
        "eoldaslib/sixs_obs/MOCA4.f", "eoldaslib/sixs_obs/MOCA5.f", \
        "eoldaslib/sixs_obs/MOCA6.f", "eoldaslib/sixs_obs/MODISALBE.f", \
        "eoldaslib/sixs_obs/MODISBRDF.f", "eoldaslib/sixs_obs/MODIS.f", \
        "eoldaslib/sixs_obs/MSS.f", "eoldaslib/sixs_obs/NIOX1.f", \
        "eoldaslib/sixs_obs/NIOX2.f", "eoldaslib/sixs_obs/NIOX3.f", \
        "eoldaslib/sixs_obs/NIOX4.f", "eoldaslib/sixs_obs/NIOX5.f", \
        "eoldaslib/sixs_obs/NIOX6.f", "eoldaslib/sixs_obs/OCEAALBE.f", \
        "eoldaslib/sixs_obs/OCEABRDF.f", "eoldaslib/sixs_obs/OCEABRDFFAST.f", \
        "eoldaslib/sixs_obs/OCEA.f", "eoldaslib/sixs_obs/OCEATOOLS.f", \
        "eoldaslib/sixs_obs/ODA550.f", "eoldaslib/sixs_obs/ODRAYL.f", \
        "eoldaslib/sixs_obs/OS.f", "eoldaslib/sixs_obs/OSPOL.f", \
        "eoldaslib/sixs_obs/OXYG3.f", "eoldaslib/sixs_obs/OXYG4.f", \
        "eoldaslib/sixs_obs/OXYG5.f", "eoldaslib/sixs_obs/OXYG6.f", \
        "eoldaslib/sixs_obs/OZON1.f", "eoldaslib/sixs_obs/PLANPOL.f", \
        "eoldaslib/sixs_obs/POLDER.f", "eoldaslib/sixs_obs/POLGLIT.f", \
        "eoldaslib/sixs_obs/POLNAD.f", "eoldaslib/sixs_obs/POSGE.f", \
        "eoldaslib/sixs_obs/POSGW.f", "eoldaslib/sixs_obs/POSLAN.f", \
        "eoldaslib/sixs_obs/POSMTO.f", "eoldaslib/sixs_obs/POSNOA.f", \
        "eoldaslib/sixs_obs/POSSOL.f", "eoldaslib/sixs_obs/POSSPO.f", 
        "eoldaslib/sixs_obs/PRESPLANE.f", "eoldaslib/sixs_obs/PRESSURE.f", \
        "eoldaslib/sixs_obs/PRINT_ERROR.f", "eoldaslib/sixs_obs/RAHMALBE.f", \
        "eoldaslib/sixs_obs/RAHMBRDF.f", "eoldaslib/sixs_obs/ROUJALBE.f", \
        "eoldaslib/sixs_obs/ROUJBRDF.f", "eoldaslib/sixs_obs/SAND.f", \
        "eoldaslib/sixs_obs/SCATRA.f", "eoldaslib/sixs_obs/SEAWIFS.f", \
        "eoldaslib/sixs_obs/SOLIRR.f", "eoldaslib/sixs_obs/SOOT.f", \
        "eoldaslib/sixs_obs/SPECINTERP.f", "eoldaslib/sixs_obs/SPLIE2.f", \
        "eoldaslib/sixs_obs/SPLIN2.f", "eoldaslib/sixs_obs/SPLINE.f", \
        "eoldaslib/sixs_obs/SPLINT.f", "eoldaslib/sixs_obs/STM.f", \
        "eoldaslib/sixs_obs/SUBSUM.f", "eoldaslib/sixs_obs/SUBWIN.f", \
        "eoldaslib/sixs_obs/TM.f", "eoldaslib/sixs_obs/TROPIC.f", \
        "eoldaslib/sixs_obs/TRUNCA.f", "eoldaslib/sixs_obs/US62.f", \
        "eoldaslib/sixs_obs/VARSOL.f", "eoldaslib/sixs_obs/VEGETA.f", \
        "eoldaslib/sixs_obs/VERSALBE.f", "eoldaslib/sixs_obs/VERSBRDF.f", \
        "eoldaslib/sixs_obs/VERSTOOLS.f", "eoldaslib/sixs_obs/VGT.f", \
        "eoldaslib/sixs_obs/VIIRS.f", "eoldaslib/sixs_obs/WALTALBE.f", \
        "eoldaslib/sixs_obs/WALTBRDF.f", "eoldaslib/sixs_obs/WATE.f", \
        "eoldaslib/sixs_obs/WAVA1.f", "eoldaslib/sixs_obs/WAVA2.f", \
        "eoldaslib/sixs_obs/WAVA3.f","eoldaslib/sixs_obs/WAVA4.f", \
        "eoldaslib/sixs_obs/WAVA5.f","eoldaslib/sixs_obs/WAVA6.f", \
        "eoldaslib/sixs_obs/sixs_mcrm_sim.f90"] )
    return config

if __name__ == "__main__":
    setup(name='sixs',
        version=version,
        description="Python bindings for 6s. The 6S code is a basic RT code used for calculation of lookup tables in the MODIS atmospheric correction algorithm.'",
        long_description="""\
    """,
        classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        keywords='remote_sensing,radiative_transfer,atmospheric_modelling',
        author='J Gomez-Dans',
        author_email='j.gomez-dans@ucl.ac.uk',
        url='http://6s.ltdri.org/',
        license='',
        packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            # -*- Extra requirements: -*-
        ],
        entry_points="""
        # -*- Entry points: -*-
        """,
        )
