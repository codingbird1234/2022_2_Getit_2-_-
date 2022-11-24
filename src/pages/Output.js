import React from "react";
//import {date, start, end, trainType, trainNum} from "input"

function Info({infoData}){
    return (
        <tr>
            <td>{infoData}</td>
        </tr>
    )
}

var infos = new Array();
var infos = [
    "[KTX 171] 11월 27일, 서울~수원(11:33~12:03) 특실,일반실 / 수원~부산(12:06~14:49) 특실,일반실",
    "[KTX 171] 11월 27일, 서울~동대구(11:33~13:58) 특실,일반실 / 동대구~부산(13:58~15:00) 특실,일반실",
];

/*
var a = new Array();
var a=["qwer","asdf","zxcv","ghjk"];
var i;
for(i = 0; i < a.lenght; i++)
{
    infos[i] = a[i];
}
*/

function Output(){
    
    return(
        <table>
            <thead>
                <tr>
                    <th>경로</th>
                </tr>
            </thead>
            <tbody>
                {infos.map(x=> <Info infoData = {x} />)}
            </tbody>
        </table>
    )
}

export default Output;