import discord
from discord.ext import commands
import random


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.command(aliases=['+'])
async def add(ctx):    #Hinzufügen von HA
    await ctx.send('Test')


@client.command(aliases=['-'])
async def delete(ctx):  #Entfernen von HA
    await ctx.send('send')


@client.command(aliases=['='])
async def list(ctx):     #Liste anzeigen

    embed = discord.Embed(title="Hausaufgaben", description="- Mathe Buch Seite 46 Nr. 2\n\n - Chemie Ha Am positiven Pol einer Zelle befinden sich 0,232g Silberoxid. Berechne die Masse an Zink für den negativen Pol (RG siehe AB)   -  das Volumen an Sauerstoff (O2) bei 20°C, wenn Silberoxid in die Elemente gespalten wird\nKunst Haus Abgabe     9. Dezember")

    await ctx.send(embed=embed)







@client.command(aliases=['googl'])
async def google(ctx, *args):
    msg = " ".join(args)

    embed = discord.Embed(title='Deine Google Suche:', description=f"https://www.google.com/search?q={msg}")

    embed.set_footer(text=f"Google Suche von {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url='https://i.pinimg.com/originals/f4/8e/7a/f48e7a6487df38a0aed24fec6c4adbff.gif')

    await ctx.send(embed=embed)

@google.error
async def google_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Bitte gebe an nach was du suchst!')

@client.command(pass_context=True)
async def facts(ctx):
    fact = ['https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1518.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1519.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1520.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1521.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1522.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1523.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1524.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1525.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1526.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1527.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1528.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1529.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1530.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1531.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1532.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1533.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1534.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1535.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1536.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/11/Fact-1537.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-51.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-53.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1737.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1738.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1739.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1740.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1741.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1742.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1743.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1744.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1745.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1746.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1747.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1337.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1338.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1339.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1340.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1341.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1342.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1343.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1344.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1345.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1346.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1347.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1348.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1349.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1350.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1351.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1352.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1353.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1354.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1355.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/07/Fact-1356.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1748.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1749.jpg',
             'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1750.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1751.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1752.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1753.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1754.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1755.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2019/06/Fact-1756.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-55.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-56.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-57.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2014/12/Fact-58.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1478.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1479.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1480.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1481.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1482.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1483.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1484.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1485.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1486.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1488.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1487.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1489.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1490.jpg',
            'https://www.bluemind.tv/wordpress/wp-content/uploads/2018/08/Fact-1491.jpg']
    embed = discord.Embed()
    embed.set_image(url=f'{random.choice(fact)}')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def meme(ctx):
    memes = ['https://i.redd.it/jt3n1vpmqjz41.jpg',
             'https://i.redd.it/a9e0j64j2kz41.jpg',
             'https://i.redd.it/qvt6iwombjz41.jpg',
             'https://i.redd.it/lzzy74x31iz41.jpg',
             'https://i.redd.it/8ccxus9p2jz41.jpg',
             'https://i.redd.it/wlpmst4zhmz41.jpg',
             'https://i.redd.it/zuhb8y2fqiz41.jpg',
             'https://i.redd.it/i4pkozf2cmz41.jpg',
             'https://i.redd.it/zgshzlvjoiz41.png',
             'https://i.redd.it/gvn4qvhkskz41.jpg',
             'https://i.redd.it/rskxqjrlglz41.jpg',
             'https://i.redd.it/7vyos3gb8iz41.jpg',
             'https://i.redd.it/rvjum51kqhz41.jpg',
             'https://i.imgur.com/17DAtWh.jpg',
             'https://i.redd.it/0d2midft7iz41.png',
             'https://i.redd.it/t5ty7ysi7jz41.jpg',
             'https://i.redd.it/m7dkt2qqafz41.jpg',
             'https://i.redd.it/fq5fiaimrjz41.png',
             'https://i.redd.it/yftr8a8c5iz41.gif',
             'https://i.redd.it/dm5jxrg5ekz41.gif',
             'https://i.redd.it/1nwhtqi2kiz41.jpg',
             'https://i.redd.it/05z631u1uiz41.jpg',
             'https://i.redd.it/3xqovk6jriz41.jpg',
             'https://i.redd.it/rmtg1npuyfz41.jpg',
             'https://i.redd.it/w0jhmxh3siz41.jpg',
             'https://i.redd.it/sfemxc030jz41.jpg',
             'https://i.redd.it/nbwc886oofz41.jpg',
             'https://i.redd.it/bhivk1drkiz41.jpg',
             'https://i.redd.it/8zls0mszojz41.jpg',
             'https://i.redd.it/26h08uaixgz41.jpg',
             'https://i.redd.it/xkdi5ykpmhz41.gif',
             'https://i.redd.it/mw1q65me0kz41.jpg',
             'https://i.redd.it/1az4rcwmzfz41.jpg',
             'https://i.redd.it/mhhed5jxxgz41.jpg',
             'https://i.redd.it/vstog5gq0gz41.jpg',
             'https://i.redd.it/efjqs3n46jz41.png',
             'https://i.redd.it/imvl0ik0vhz41.jpg',
             'https://i.redd.it/mfb1hoa6cfz41.jpg',
             'https://i.redd.it/45cpalc5biz41.gif',
             'https://i.redd.it/zze7i8h5mgz41.jpg',
             'https://i.redd.it/pjqkgf39hfz41.png',
             'https://i.redd.it/ivordrzhniz41.jpg',
             'https://i.redd.it/0u4qv7xbpgz41.jpg',
             'https://i.redd.it/d7dy67287hz41.jpg',
             'https://i.redd.it/82b6esmrpkz41.jpg',
             'https://i.redd.it/t5lec9olthz41.jpg',
             'https://i.redd.it/fqtrm7559kz41.jpg',
             'https://i.redd.it/hmgrr26byiz41.jpg',
             'https://i.redd.it/3t73af0g0hz41.jpg',
             'https://i.redd.it/z4g3jtu8vfz41.jpg',
             'https://i.redd.it/gtuv5twr1hz41.png',
             'https://i.redd.it/uf5uefui1lz41.jpg',
             'https://i.redd.it/52ug91jczhz41.png',
             'https://i.redd.it/vz7w7m5hwfz41.jpg',
             'https://i.redd.it/osb5yj9l2hz41.png']
    embed = discord.Embed()
    embed.set_image(url=f'{random.choice(memes)}')
    await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Angefordert von {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Servername", value=member.display_name)

    embed.add_field(name="Erstellt am:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Beigetreten am:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Rollen ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top Rollen:", value=member.top_role.mention)

    await ctx.send(embed=embed)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Bitte pinge einen User!{ctx.author.mention}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count=2):
    if ctx.message.author.bot == False:
        deleted = await ctx.message.channel.purge(limit=count + 1)
        message = await ctx.message.channel.send(f"Es wurden {len(deleted) - 1} Nachricht(en) gelöscht!")
        await asyncio.sleep(3)
        await message.delete()


client.run('NzgwNzQxMDAxMDAyMjIxNTY4.X7zfuA.3q18UZpA9zpqaz1KJyF-lB8Y6Gs')