import React,{useState} from "react";
import styles from "./Input.module.css";

function Input(){
    const [inputs,setInputs]=useState({
        date: "", //id
        start: "",
        end: "",
        trainType: "",
        trainNum: ""
    });

    const {date, start, end, trainType, trainNum} = inputs;

    function onChange(e) {
        const value = e.target.value;
        const id = e.target.id;

        setInputs({
            ...inputs, //deepcopy
            [id]: value
        })
    };

    return (
        <div>
            <div>
                <br></br>
            </div>
            <div>
                <label>날짜</label>
                <input type="date" id="date" value={date} onChange={onChange}/>
            </div>
            <div>
                <label>출발지</label>
                <input type="start" id="start" value={start} onChange={onChange}/>
            </div>
            <div>
                <label>도착지</label>
                <input type="end" id="end" value={end} onChange={onChange}/>
            </div>
            <div>
                <label>기차종류</label>
                <input type="trainType" id="trainType" value={trainType} onChange={onChange}/>
            </div>
            <div>
                <label>기차번호</label>
                <input type="trainNum" id="trainNum" value={trainNum} onChange={onChange}/>
            </div>
            <div> <br></br></div>
        </div>
    );
};

export default Input;