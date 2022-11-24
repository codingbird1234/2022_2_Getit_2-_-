import React,{useState} from "react";
import styles from "./Input.module.css";

function Login(){
    const [inputs,setInputs]=useState({
        Id: "", //id
        pw: "",
    });

    const {Id,pw} = inputs;

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
                <label>아이디</label>
                <input type="Id" id="Id" value={Id} onChange={onChange}/>
            </div>
            <div>
                <label>비밀번호</label>
                <input type="pw" id="pw" value={pw} onChange={onChange}/>
            </div>
            <div> <br></br></div>
        </div>
    );
};

export default Login;