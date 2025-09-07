import puppeteer from "puppeteer";

const url = "https://iporesult.cdsc.com.np/";

const main = async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);

    const data = await page.evaluate(() => {
        const datas = document.querySelectorAll('img');
        return Array.from(datas)
    } )


    await browser.close();

}
main();