
import './App.css';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import RadioGroup from '@mui/material/RadioGroup';
import Radio from '@mui/material/Radio';
function App() {
  let MCQprompt = "This is the question of the MCQ"
  let choices = ["first choice","second choice","third choice","fourth choice"]
  return (
    <div>
      <meta name="viewport" content="initial-scale=1, width=device-width" />
      <Typography fullwidth component="h1" variant="h5">
        {MCQprompt}
      </Typography>
      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="female"
        name="radio-buttons-group"
      >
        <FormControlLabel value="option1" control={<Radio />} label={choices[0]} />
        <FormControlLabel value="option2" control={<Radio />} label={choices[1]} />
        <FormControlLabel value="option3" control={<Radio />} label={choices[2]} />
        <FormControlLabel value="option4" control={<Radio />} label={choices[3]}/>
      </RadioGroup>
    </div>
  );
}

export default App;
