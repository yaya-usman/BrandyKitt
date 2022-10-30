import Head from 'next/head'
import Image from 'next/image'
import BrandyKitt from '../components/BrandyKitt'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>BrandyKitt | Next-level AI assisted branding snippet generator.</title>
        <meta name="description" content="BrandyKitt | Next-level AI assisted branding snippet generator" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <BrandyKitt />
    </div>
  )
}
