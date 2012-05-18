
      SUBROUTINE run_sixs_mcrm ( ULI, EEI, THMI, SLI, CABI, CWI, VAII, &
     & RNCI, RSL1I, LAMBDA, SZA, SAZ, VZA, VAZ, BRDF_S, BRDF_V, ALBBRDF, &
     & SBRDF )
      

      IMPLICIT NONE


     INTEGER, parameter :: MU_P = 11
     INTEGER, PARAMETER :: NP_P = 13
     INTEGER :: I,J,K,MU,NP,MUM1,COUNTER

      DOUBLE PRECISION, INTENT(OUT) :: SBRDF(1),ALBBRDF
      DOUBLE PRECISION, intent(IN) :: LAMBDA(1), SZA, SAZ, VZA, VAZ
      DOUBLE PRECISION, intent(IN) :: ULI,EEI,THMI,SLI,CABI,CWI,VAII,RNCI,RSL1I
      DOUBLE PRECISION, intent (out), dimension ( mu_p, np_p ) :: brdf_v, brdf_s

      DOUBLE PRECISION :: BRDFINTS(-MU_P:MU_P,NP_P)
      DOUBLE PRECISION :: BRDFINTV(-MU_P:MU_P,NP_P)
      DOUBLE PRECISION :: SRM(-1:1),SRP(1),RM(-MU_P:MU_P),RP(NP_P)
      DOUBLE PRECISION :: PI,TWOPI,PHIRAD,XMUS,XMUV,XMUP
      DOUBLE PRECISION :: ANGLEM(2*(MU_P-1))
      DOUBLE PRECISION, dimension(MU_P-1) :: ANGMU = (/85.0,80.0,70.0, &
     & 60.0,50.0,40.0, 30.0,20.0,10.0,0.00/)
      DOUBLE PRECISION, dimension (NP_P) :: ANGPHI = (/0.00, 30.0,60.0,90.0, &
     & 120.0,150.0, 180.0, 210.0,240.0,270.0,300.0,330.0,360.0/)
      DOUBLE PRECISION :: SBRDFTMP(-1:1,1)
      REAL :: ULIr,EEIr,THMIr,SLIr,CABIr,CWIr,VAIIr,RNCIr,RSL1Ir, lambdar(1)
      

! SETUP SOME PARAMETER AND USEFUL COMBINATIONS 
      PI = 3.141592653589793
      TWOPI = 2.*PI
! COPY PARAMETERS INTO VARIABLES FOR SUBROUTINE CALLS
      MU = MU_P
      NP = NP_P
! CONVERT RELATIVE AZIMUTH TO RADIANS AND TAKE SOME COSINES
      PHIRAD = (saz - sza )*pi/180.
      if (PHIRAD.LT.0.) PHIRAD = PHIRAD + 2.*PI
      if (PHIRAD.GT.(2.*PI)) PHIRAD = PHIRAD - 2.*PI
      XMUS=COS(sza*PI/180.)
      XMUV=COS(vza*PI/180.)
      XMUP=COS(PHIRAD)

    ulir = real(uli)
    eeir = real ( eei )
    thmir = real ( thmi )
    slir = real ( sli )
    cabir = real ( cabi )
    cwir = real ( cwi )
    vaiir = real ( vaii )
    rncir = real ( rnci )
    rsl1ir = real ( rsl1i )
    lambdar = real ( lambda )
!      CALL GAUSS(-1.,1.,ANGLEM,WEIGHTM,2*(MU-1))
!      CALL GAUSS(0.,TWOPI,RP,GP,NP)
! PUT THE REGULARLY SPACED AZIMUTH ANGLES INTO THE RP ARRAY AS RADIANS
      DO J=1,NP
        RP(J)=ANGPHI(J)*PI/180.
      ENDDO

! PUT COS(REGULAR ZENITH ANGLE GRID) INTO RM ARRAY
! RM (-mu+1:-1) RUNS OVER RANGE (95,100,110...170,180)
! RM (1:MU)     RUNS OVER RANGE (0,10,20,...80,85)
      MUM1=MU-1
      DO 581 J=-MUM1,-1
       K=MU+J
       RM(-J-MU)=COS(180-ANGMU(-J)*PI/180)
  581 CONTINUE
      DO 582 J=1,MUM1
       K=MU-J
       RM(J)=COS(ANGMU(K)*PI/180)
  582 CONTINUE
      !WRITE(6,*) RM
      !PAUSE
      SRM(-1)=PHIRAD
      SRM(1)=XMUV
      SRM(0)=XMUS 
      
      CALL AKBRDF(EEIr,THMIr,ULIr,SLIr,RSL1Ir,LAMBDAr,RNCIr,CABIr,CWIr,VAIIr, &
     &      1,1,SRM,SRP,SBRDFTMP)
      SBRDF(1)=SBRDFTMP(1,1)

      RM(-MU)=PHIRAD
      RM(MU) =XMUV
      RM(0)  =XMUS
      
      CALL AKBRDF(EEIr,THMIr,ULIr,SLIr,RSL1Ir,LAMBDAr,RNCIr,CABIr,CWIr,VAIIr, &
     &            MU,NP,RM,RP,BRDFINTS)
      RM(-MU)=2.*PI-PHIRAD
      RM(MU) =XMUS
      RM(0)  =XMUV
      
      CALL AKBRDF(EEIr,THMIr,ULIr,SLIr,RSL1Ir,LAMBDAr,RNCIr,CABIr,CWIr,VAIIr, &
     &            MU,NP,RM,RP,BRDFINTV)
      CALL AKALBE(ALBBRDF)
    
!       do i = 1, mu_p
!          do j = 1, np_p
!             brdf_v ( i, j ) = brdfintv ( i, j )
!             brdf_s ( i, j ) = brdfints ( i, j )
!          end do
!       end do
            
      do j = 1, 13
!        write ( 6, * )(brdfintv(i,j),i=1,10)
        do i = 1, 11
            brdf_v ( i, j ) = real(brdfintv(i,j))
        end do
      end do
      
      do j = 1, 13
!        write ( 6, * )(brdfints(i,j),i=1,10)
        do i = 1, 11
            brdf_s ( i, j ) = real(brdfints(i,j))
        end do
        
      end do
    END SUBROUTINE run_sixs_mcrm
