import React from "react";

function Margins({ propClass, children }) {
  return <div className={`margins-container layout-container ${propClass?? ""}`}>{children}</div>;
}

export default Margins;
