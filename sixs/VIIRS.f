      subroutine viirs(iwa)
      common /sixs_ffu/ s(1501),wlinf,wlsup
      real sr(16,1501),wli(16),wls(16)
      real wlinf,wlsup,s
      integer iwa,l,i
   
c
c    VIIRS band M1
c
      data (sr(1,l),l=1,1501)/ 61*0.,
     a 0.7,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,0.3,
     a1431*0./
c
c    VIIRS band M2
c
      data (sr(2,l),l=1,1501) / 74*0.,
     a 0.1,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,0.1,
     a1418*0./
c
c    VIIRS band M3
c
      data (sr(3,l),l=1,1501)/ 91*0.,
     a 0.3,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,0.7,
     a1401*0./
c
c    VIIRS band M4
c
      data (sr(4,l),l=1,1501)/ 118*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,0.5,
     a1374*0./
c
c    VIIRS band M5
c
      data (sr(5,l),l=1,1501)/ 165*0.,
     a 0.7,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,0.3,
     a1327*0./
c
c    VIIRS band M6
c
      data (sr(6,l),l=1,1501)/ 195*0.,
     a 0.1,1.0,1.0,1.0,1.0,
     a 1.0,0.9,
     a1299*0./
c
c    VIIRS band M7
c
      data (sr(7,l),l=1,1501)/ 238*0.,
     a 0.3,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,0.3,
     a1246*0./
c
c    VIIRS band M8
c
      data (sr(8,l),l=1,1501)/ 392*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,0.5,
     a1100*0./
c
c    VIIRS band M9
c
      data (sr(9,l),l=1,1501)/ 448*0.,
     a 0.3,1.0,1.0,1.0,1.0,
     a 1.0,0.7,
     a1046*0./
c
c    VIIRS band M10
c
      data (sr(10,l),l=1,1501)/ 532*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,0.5,
     a944*0./
c
c    VIIRS band M11
c
      data (sr(11,l),l=1,1501)/ 790*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 0.5,
     a690*0./
c
c    VIIRS band M12
c
      data (sr(12,l),l=1,1501)/ 1344*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,0.5,
     a84*0./
c
c    VIIRS band I1
c
      data (sr(13,l),l=1,1501)/ 140*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,0.5,
     a1328*0./
c
c    VIIRS band I2
c
      data (sr(14,l),l=1,1501)/ 238*0.,
     a 0.3,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,0.3,
     a1246*0./
c
c    VIIRS band I3
c
      data (sr(15,l),l=1,1501)/ 532*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,0.5,
     a944*0./
c
c    VIIRS band I4
c
      data (sr(16,l),l=1,1501)/ 1320*0.,
     a 0.5,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,1.0,1.0,1.0,
     a 1.0,1.0,0.5,
     a28*0./
 
c
      wli(1)=0.4025
      wls(1)=0.4225
      wli(2)=0.4350
      wls(2)=0.4550
      wli(3)=0.4775
      wls(3)=0.4975
      wli(4)=0.5450
      wls(4)=0.5650
      wli(5)=0.6625
      wls(5)=0.6825
      wli(6)=0.7375
      wls(6)=0.7525
      wli(7)=0.8450
      wls(7)=0.8850
      wli(8)=1.2300
      wls(8)=1.2500
      wli(9)=1.3700
      wls(9)=1.3850
      wli(10)=1.5800
      wls(10)=1.6400
      wli(11)=2.2250
      wls(11)=2.2750
      wli(12)=3.6100
      wls(12)=3.7900
      wli(13)=0.6000
      wls(13)=0.6800
      wli(14)=0.8450
      wls(14)=0.8850
      wli(15)=1.5800
      wls(15)=1.6400
      wli(16)=3.5500
      wls(16)=3.9300
      do 1 i=1,1501
      s(i)=sr(iwa,i)
    1 continue
      wlinf=wli(iwa)
      wlsup=wls(iwa)
      return
      end
