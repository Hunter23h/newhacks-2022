import React, { useState } from "react";
import LOGO from "../assets/Logo.png";
import axios from "axios";
import { useEffect } from "react";
function LandingPage({sendData, scrollTo}) {
  
  const [link, setLink] = useState("");
  const [summarySize, setSummarySize] = useState(5);
  const [paused, setPaused] = useState(false);
  


  const getData = async (props) => {
    try {
      setPaused(true);
      let res = await axios.post(
        "/getdata",
        {
          link,
          summarySize,
        }
      );
      let resData = res.data;
      console.log(resData);
      sendData(resData);
      setPaused(false);
      scrollTo("article");
    } catch (e) {
      console.log(e);
      setPaused(false);
      alert("Website invalid.")
    }
  };

  const changeSummarySize = (val) => {
    if (
      parseFloat(summarySize) + parseFloat(val) > 15 ||
      parseFloat(summarySize) + parseFloat(val) < 1
    ) {
      return;
    }
    let result = parseFloat(summarySize) + parseFloat(val)
    setSummarySize(parseFloat(summarySize) + parseFloat(val));
  };

  return (
    <div className="landing-page col-c-c">
      <img className="mb-10" src={LOGO} alt="Logo" />
      <div className="landing-page-content pb-12">
        <h1 className="text-center">
          Eliminate Unreliable Sources <br className="br-title"/>
          and Establish Credibility.
        </h1>
        <p className="text-center text-xl pt-1">
          Don't know if an article is unreliable? Want a quick summary of the article? Want an MLA formatted citation? Paste the link below and get all the answers.
        </p>
      </div>
      <input
        className="landing-page-url pl-4 py-3 text-center"
        type="text"
        placeholder="Article URL Link"
        onChange={(e) => {
          setLink(e.target.value);
        }}
        readOnly={paused}
      />
      <label className="col-c-c mt-5">
        <span>Summary Size</span>
        <div className="landing-page-summary-size-buttons row-c-c">
          <button
            className="summary-size-decrement"
            onClick={() => {
              changeSummarySize(-1);
            }}
          >
            -
          </button>
          <input
            type="text"
            className="landing-page-summary-size py-2 text-center"
            placeholder="1"
            value={summarySize}
            readOnly={true}
          />
          <button
            className="summary-size-increment"
            onClick={() => {
              changeSummarySize(1);
            }}
          >
            +
          </button>
        </div>
      </label>
      <div className="landing-page-btns row-c-c">
        {paused ? (
          <div className="landing-page-validate dots row-c-c mt-8 py-4">
            <div className="dot1"></div>
            <div className="dot2"></div>
            <div className="dot3"></div>
          </div>
        ) : (
          <button
            className="landing-page-validate mt-8 py-1"
            onClick={() => {
              getData(link);
            }}
          >
            Validate
          </button>
        )}
      </div>
    </div>
  );
}

export default LandingPage;
