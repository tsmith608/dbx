000100260302     H DFTACTGRP(*NO) ACTGRP('GANDR')
000200260302     FORDERS    UF   E           K DISK
000300260302     FMYLIBSRC  O    E             PRINTER
000400260302
000500260302     D OrderVal        PR
000600260302     D  pOrderNum                    9P 0
000700260302
000800260302     D OrderVal        PI
000900260302     D  pOrderNum                    9P 0
001000260302
001100260302      /FREE
001200260302
001300260302        chain pOrderNum ORDERS;
001400260302
001500260302        if %found(ORDERS);
001600260302           // Check Order Status
001700260302           if ORDSTS = 'P';
001800260302              exsr ProcessOrder;
001900260302           else;
002000260302              DSPLY 'Order not in Pending status';
002100260302           endif;
002200260302        else;
002300260302           DSPLY 'Order not found';
002400260302        endif;
002500260302
002600260302        *INLR = *ON;
002700260302        return;
002800260302
002900260302        begsr ProcessOrder;
003000260302           // Legacy processing logic
003100260302           ORDSTS = 'S'; // Shipped
003200260302           update ORDERS;
003300260302        endsr;
003400260302
003500260302      /END-FREE