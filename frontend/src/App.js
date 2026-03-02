import { useEffect, useState } from "react";
import "./App.css";
const API_URL = process.env.REACT_APP_BACKEND_URI;
function App() {
  const [movieList, setMovieList] = useState([]);
  const [movies, setMovies] = useState([]);
  const [featured, setFeatured] = useState(null);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    fetch(`${API_URL}/movies`)
      .then((res) => res.json())
      .then((data) => setMovieList(data.movies));
    handleSearch("Avatar");
  }, []);

  const handleSearch = async (movie) => {
    setLoading(true);
    const response = await fetch(`${API_URL}/recommend/${movie}`);

    const data = await response.json();

    setFeatured({
      title: movie,
      backdrop: data.recommendations[5]?.backdrop,
      description: data.recommendations[5]?.description,
      poster: data.recommendations[5]?.poster_main,
    });

    setMovies(data.recommendations);
    setLoading(false);
  };

  return (
    <div className="app">
      <Navbar movies={movieList} onSearch={handleSearch} />
      {loading && <div className="loader"></div>}
      {featured && <Hero movie={featured} />}
      <MovieRow movies={movies} onSelect={handleSearch} />
    </div>
  );
}

function Navbar({ movies, onSearch }) {
  return (
    <div className="navbar">
      <h2 className="logo">MovieFlix</h2>

      <input
        className="search-input"
        list="movie-options"
        placeholder="Search movie..."
        onChange={(e) => {
          if (movies.includes(e.target.value)) {
            onSearch(e.target.value);
          }
        }}
      />

      <datalist id="movie-options">
        {movies.map((movie, index) => (
          <option key={index} value={movie} />
        ))}
      </datalist>
    </div>
  );
}

function Hero({ movie }) {
  return (
    <div
      className="hero"
      style={{
        backgroundImage: `url(${movie.backdrop})`,
      }}
    >
      <div className="hero-overlay">
        <div className="poster-container">
          <img src={movie.poster} alt={movie.title} className="poster-main" />
        </div>
        <div className="movie-info">
          <h1>{movie.title}</h1>
          <h5 className="description">{movie.description}</h5>
        </div>
      </div>
    </div>
  );
}

function MovieRow({ movies, onSelect }) {
  return (
    <div className="row">
      <h3>You might also like:</h3>
      <div className="row-posters">
        {movies.map((movie, index) => (
          <img
            key={index}
            src={movie.poster}
            alt={movie.title}
            onClick={() => onSelect(movie.title)}
            style={{ cursor: "pointer" }}
            className="poster"
          />
        ))}
      </div>
    </div>
  );
}

export default App;
