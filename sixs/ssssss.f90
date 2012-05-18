subroutine ssssss(x,xrad,xa,xb,xc)
    integer,parameter :: ibignumber = 1000
    double precision x(ibignumber)
    double precision, intent(out) :: xrad,xa,xb,xc

! Final argument =0 flags for no screen output from the 6S code
    call main_ssssss(x,xrad,xa,xb,xc,0)

end subroutine ssssss
