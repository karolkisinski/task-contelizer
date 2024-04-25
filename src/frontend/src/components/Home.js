import { useNavigate } from "react-router-dom"


export const Home = () => {
    const navigate = useNavigate()
    return (
        <>
            <div>Home Page</div>
            <button onClick={() => navigate('text-random')}>Text</button>
            <button onClick={() => navigate('pesel-validator')}>Pesel</button>
        </>
    )
}