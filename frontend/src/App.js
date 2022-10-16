import React, { useEffect, useState } from "react";

function App() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);
  
  useEffect(() => {
    fetch("http://localhost:5000/")
    .then(res => res.json())
    .then(
      (result) => {
        setIsLoaded(true);
        setItems(result.Users);
      },

      (error) => {
        setIsLoaded(true);
        setError(error);
      }
      )
  }, [])
  
  if (error) {
    return <div>Error: {error.message}</div>;
  } else if (!isLoaded) {
    return <div>Loading...</div>;
  } else {
    return (
      <div>USERS
        <ul>
          {items.map(item => (
            <li key={item.id}>
              {item.name}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;