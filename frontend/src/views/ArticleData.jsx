import React from "react";
import { useEffect } from "react";
import { Bar } from "react-chartjs-2";
import { Doughnut } from "react-chartjs-2";
import { Chart, ArcElement } from "chart.js";
Chart.register(ArcElement);
function ArticleData(props) {
  const data = {
    labels: ["Right", "Wrong"],
    datasets: [
      {
        label: "Price in USD",
        data: [props.data.score, 10-props.data.score],
        backgroundColor: ["#3b9b80", "#D62828"],
      },
    ],
  };
  return (
    <div className="article-data col-fs-c">
      <h1 className="text-center text-5xl pt-5 pb-10 ">Article Analysis</h1>
      <div className="article-layout pb-7">
        <div className="article-data-reliability col-c-c">
          <h2>Reliability Score</h2>
          <p className="reliability-score">{props.data.score}</p>
          <div className="data-score row-c-c">
            <Doughnut data={data} />
          </div>
        </div>
        <div className="article-data-citation pb-10 col-fs-c">
          <h2 className="">Citation</h2>
          <p className="citation">
            <p>{props.data.MLA}</p>
          </p>
        </div>
        <div className="article-data-summary col-fs-c">
          <h2>Article Summary</h2>
          <p className="summary pb-10">
            <p>{props.data.summary}</p>
          </p>
        </div>
      </div>
    </div>
  );
}

export default ArticleData;
