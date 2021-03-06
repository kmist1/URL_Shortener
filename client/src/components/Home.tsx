import React from 'react';
import {createStyles, makeStyles, Theme} from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import Container from "@material-ui/core/Container";
import Button from '@material-ui/core/Button';
import Axios from "axios";

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            backgroundColor: 'black',
            backgroundSize:'1500px',
            display:'flex',
            height: theme.spacing(100),
            flexDirection:'row',
        },

        pageContainer: {
            marginTop: theme.spacing(5),
        },

        section1: {
            flexDirection:'column',
            top:'20%',
            left:'35%',
            zIndex: theme.spacing(2),
            position:'absolute',
        },

        section2: {
            color:'white',
            fontWeight:'bold',
            textAlign:'center',
        },

        section3: {
            color:'white',

        }
    }),
);


interface State {
    LongURL: string,
    Email: string,
    submitFlag: boolean
}


export default function Home() {

    const classes = useStyles();

    const [values, setValues] = React.useState<State>({
        LongURL:'',
        Email:'',
        submitFlag: false,
    });

    const handleEmailChange = (event: any) => {
        return setValues({...values, Email: event.target.value})
    };

    const handleLongURLChange = (event: any) => {
        return setValues({...values, LongURL: event.target.value})
    };

    const handleSubmit = () => {setValues({...values, submitFlag :true})};

    React.useEffect(() => {
        if(values.submitFlag){
            
            (async ()=> {
                try {
                    const data = {Email:values.Email, LongLink:values.LongURL};
                    const response = await Axios.post('/links',data);
                    if (response.status === 200) {
                        alert(`Here is your sort link: ${response.data['sort_link']}`);
                    }
                }
                catch (e) {
                    if (e.message === 'Request failed with status code 400') {
                        alert(`Failed to create sort URL, Please make sure long url not used before`);
                    }
                    else alert(`something wrong with server, Please contact us`);
                }
            })();
            
        }
    },[values.submitFlag]);

    return (
            <div className={classes.root}>
            <React.Fragment>
                <CssBaseline />
                <Container fixed className={classes.pageContainer}>
                    <div>
                        <div className = {classes.section1}>
                            <div className={classes.section2} style={{backgroundColor:'rgba(0,0,0, 0.4)'}}>
                                <h1 style={{fontSize: '60px'}}> URL Shortener</h1>
                            </div>
                            <form>
                                <div className = {classes.section3}>
                                    <input 
                                        type="text"
                                        value = {values.LongURL}
                                        onChange={handleLongURLChange}
                                        placeholder= "Long URL"
                                        style={{ width:"100%", padding:"12px 20px", margin :"8px 0", color :"black", border:'2px solid grey',borderRadius:'7px'}}
                                    />
                                    <input 
                                        type="text"
                                        value = {values.Email}
                                        onChange = {handleEmailChange}
                                        placeholder= "Email"
                                        style={{ width:"100%", padding:"12px 20px", margin :"8px 0", color :"black", border:'2px solid grey', borderRadius:'7px'}}
                                    />
                                    <Button 
                                        variant="contained"
                                        onClick={handleSubmit}
                                        style={{
                                            width:'100%',
                                            marginBottom:'-20%',
                                            boxShadow: '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)',
                                            fontWeight: 'bold',
                                            font: 'fantasy'
                                        }}
                                    >Short It
                                    </Button>
                                </div>
                            </form>
                        </div>      
                    </div>
                </Container>
            </React.Fragment>
        </div>
    );
}